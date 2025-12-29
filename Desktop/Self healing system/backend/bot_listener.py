import requests
import os

BOT = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT = os.getenv("TELEGRAM_CHAT_ID")

def activate_bot():
    url = f"https://api.telegram.org/bot{BOT}/sendMessage"
    payload = {
        "chat_id": CHAT,
        "text": "🔥 Bot Activated! Alerts are now enabled."
    }
    response = requests.post(url, data=payload)
    print(response.text)
