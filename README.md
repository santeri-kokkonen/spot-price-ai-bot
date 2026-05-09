# AI-Powered Electricity Price Bot

Lightweight, autonomous Python application designed to optimize daily electricity consumption. The project solves a practical everyday problem by fetching raw spot electricity prices, processing the time-series data, and utilizing a Large Language Model (LLM) to generate a personalized, human-readable optimization report delivered directly to a mobile device.

I made this AI-powered automation bot because I wanted to get daily, AI-analyzed spot electricity prices delivered straight to my phone, completely eliminating the hassle of manually checking different apps. This project demonstrates practical skills in REST API integration, data manipulation, prompt engineering, and automated notifications.

## Tech Stack
- **Core language:** Python
- **Data processing:** pandas (timezone conversions, time-series filtering, data formatting)
- **AI integration:** Google GenAI SDK / Gemini 2.5 Flash (prompt engineering, text generation)
- **API communication:** requests (fetching JSON data from public APIs)
- **Notifications:** Telegram Bot API (automated message delivery)
- **Configuration:** python-dotenv (secure environment variable management)

## Quick Start
1. **Clone & Install:** Clone the repository, create a virtual environment, and run `pip install -r requirements.txt`.
2. **Environment Variables:** Create a `.env` file in the root with your credentials (`GEMINI_API_KEY`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`).
3. **Configure AI:** Create a `prompt.txt` file containing the AI instructions. Make sure to include the `{ai_data}` placeholder for the dataset.
4. **Execute:** Run `python main.py` to trigger the pipeline.
