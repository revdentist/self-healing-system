import requests
import os
from dotenv import load_dotenv

load_dotenv()

def send_telegram_alert(message: str):
    bot = os.getenv("TELEGRAM_BOT_TOKEN")
    chat = os.getenv("TELEGRAM_CHAT_ID")

    if not bot or not chat:
        return

    url = f"https://api.telegram.org/bot{bot}/sendMessage"
    payload = {
        "chat_id": chat,
        "text": message
    }

    requests.post(url, data=payload)
