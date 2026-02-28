import os
import subprocess

from google import genai
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_price_data() -> pd.DataFrame:
    """
    Fetches electricity prices from the Pörssisähkö.net API and returns them as a pandas DataFrame.
    """

    url = "https://api.porssisahko.net/v2/latest-prices.json"
    response = requests.get(url)

    if response.status_code == 200:
        # Convert the JSON response into a Python dictionary and
        # extract the "prices" key, which contains the list of price intervals.
        data: dict = response.json()
        price_intervals = data["prices"]

        # Create a pandas DataFrame from the price data.
        df: pd.DataFrame = pd.DataFrame(price_intervals)

        # Drop the useless endDate column, we don't need it.
        df.drop(columns=["endDate"], inplace=True)

        # Convert the startDate to a datetime object and shift it to Finnish local time.
        df["startDate"] = pd.to_datetime(
            df["startDate"]).dt.tz_convert("Europe/Helsinki")

        # Sort the DataFrame ascending by startDate (0, 1, 2...).
        df.sort_values(by="startDate", ascending=True, inplace=True)

        # Filter the DataFrame to keep only future price intervals (where startDate > right now).
        now = pd.Timestamp.now(tz="Europe/Helsinki")
        df = df[df["startDate"] > now]
        df = df.reset_index(drop=True)

        # Return the fully processed DataFrame.
        return df

    else:
        raise requests.RequestException(
            f"Error fetching electricity prices. Status code: {response.status_code}")


def get_aatos_insights(df: pd.DataFrame) -> str:
    """Analyzes the electricity price data using AI and generates a report text."""

    # 1. Convert the DataFrame to markdown format so the AI can read it easily.
    ai_data = df.to_markdown(index=False)

    # 2. Read the prompt file and inject the markdown data into it.
    with open("prompt.txt", "r", encoding="utf-8") as file:
        prompt = file.read()
        prompt = prompt.replace("{ai_data}", ai_data)

    # 3. Send the request to Gemini
    report = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt)

    # 4. Return the generated report as a string
    return str(report.text)


def send_telegram_message(message: str) -> None:
    """Sends a text message to Telegram via the bot."""

    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    payload: dict = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }

    # Dispatch the payload to Telegram
    response = requests.post(url, json=payload)

    # Check the response status and print the appropriate message
    if response.status_code == 200:
        print("Report successfully delivered to Telegram!")
    else:
        print(f"Error during Telegram dispatch: {response.text}")


def tulosta_aatos_logo() -> None:
    """Prints the Aatos logo and welcome message to the terminal."""

    # Clear the terminal safely based on the OS
    if os.name == 'nt':
        subprocess.run("cls", shell=True, check=False)
    else:
        subprocess.run("clear", shell=True, check=False)

    # Centered logo with top border and bulletproof double-backslashes
    logo = """
  =================================================
          _        _  _____  ___  ____  
         / \\      / \\|_   _|/ _ \\/ ___| 
        / _ \\    / _ \\ | | | | | \\___ \\ 
       / ___ \\  / ___ \\| | | |_| |___) |
      /_/   \\_\\/_/   \\_\\_|  \\___/|____/ 
                                        
  ADVANCED AUTONOMOUS TECHNICAL OPTIMIZATION SYSTEM
  =================================================
    """

    # Print in green
    print(f"\033[92m{logo}\033[0m")
    print("  >> System activated.")
    print("  >> Spot electricity data loaded and formatted.")
    print("  >> Aatos is analyzing the market situation, please wait...\n")


def main() -> None:
    """Main function that orchestrates the execution."""

    tulosta_aatos_logo()

    df = get_price_data()

    report = get_aatos_insights(df)

    # Send the final report to Telegram
    send_telegram_message(report)

    print(report)


# Run the main function only if this script is executed directly
if __name__ == "__main__":
    main()
