# Aatos - AI-Powered Electricity price Bot

**Aatos** is a lightweight, autonomous Python application designed to optimize daily electricity consumption. The project solves a practical everyday problem by fetching raw spot electricity prices, processing the time-series data, and utilizing a Large Language Model (LLM) to generate a personalized, human-readable optimization report delivered directly to a mobile device.

I made this AI-Powered Automation Bot because I wanted to get daily, AI-analyzed spot electricity prices delivered straight to my phone, completely eliminating the hassle of manually checking different apps. This project demonstrates practical skills in REST API integration, data manipulation, prompt engineering, and automated notifications.

### Tech Stack
* **Core Language:** Python 3
* **Data Processing:** Pandas (Time-zone conversions, time-series filtering, data formatting)
* **AI Integration:** Google GenAI SDK / Gemini 2.5 Flash (Prompt engineering, text generation)
* **API Communication:** Requests (Fetching JSON data from public APIs)
* **Notifications:** Telegram Bot API (Automated message delivery)
* **Configuration:** `python-dotenv` (Secure environment variable management)

### Quick Start
1. **Clone & Install:** `git clone` the repository, create a virtual environment, and run `pip install -r requirements.txt`.
2. **Environment Variables:** Create a `.env` file in the root with your credentials (`GEMINI_API_KEY`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`).
3. **Configure AI:** Create a `prompt.txt` file containing the AI instructions (include `{ai_data}` placeholder for the dataset).
4. **Execute:** Run `python main.py` to trigger the pipeline.

---

# Aatos - Tekoälypohjainen Sähkönhintabotti

**Aatos** on kevyt ja autonominen Python-sovellus, joka on suunniteltu optimoimaan päivittäistä sähkönkulutusta. Projekti ratkaisee käytännön ongelman hakemalla pörssisähkön raakadatan, käsittelemällä aikasarjatiedon ja hyödyntämällä LLM:ää luodakseen personoidun, selkokielisen sähkön käytön optimointiraportin suoraan puhelimeen.

Tein tämän tekoälyavusteisen automaatiobotin, koska halusin saada päivittäiset pörssisähkön hinnat valmiiksi analysoituna suoraan puhelimeeni täysin automaattisesti ja ilman minkäänlaista ylimääräistä säätöä. Tämä projekti demonstroi osaamista REST API -integraatioissa, datan käsittelyssä, prompt engineeringissä sekä automaattisissa ilmoituksissa.

### Tech Stack
* **Pääkieli:** Python 3
* **Datan käsittely:** Pandas (Aikavyöhykkeiden muunnokset, aikasarjojen suodatus, formatointi)
* **Tekoäly:** Google GenAI SDK / Gemini 2.5 Flash (Kehotteiden hallinta, tekstin generointi)
* **API-liikenne:** Requests (JSON-datan noutaminen julkisista rajapinnoista)
* **Ilmoitukset:** Telegram Bot API (Automaattinen viestien välitys)
* **Konfiguraatio:** `python-dotenv` (Ympäristömuuttujien ja salaisuuksien turvallinen hallinta)

### Pikaohje
1. **Kloonaa ja asenna:** Aja `git clone`, luo virtuaaliympäristö ja suorita `pip install -r requirements.txt`.
2. **Ympäristömuuttujat:** Luo juurikansioon `.env`-tiedosto ja lisää avaimesi (`GEMINI_API_KEY`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`).
3. **Tekoälyn asetukset:** Luo `prompt.txt`-tiedosto, johon kirjoitat tekoälyn ohjeet (sisällytä `{ai_data}`-paikkamerkki datalle).
4. **Suorita:** Käynnistä ohjelma komennolla `python main.py`.