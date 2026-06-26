import requests
from config import TELEGRAM_TOKEN, CHAT_ID


def send_telegram(message):

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=10
        )

        if response.status_code == 200:
            print("✅ Telegram sent")
            return True
        else:
            print("Telegram Error:", response.text)
            return False

    except Exception as e:
        print(e)
        return False


def build_signal_message(
    pair,
    signal,
    grade,
    score,
    entry,
    sl,
    tp1,
    tp2,
    trend_h1,
    trend_h4,
    divergence
):

    message = f"""
🚨 <b>{signal}</b> ({grade})

📈 Pair: <b>{pair}</b>

💰 Entry : <b>{entry:.5f}</b>

🛑 Stop Loss : <b>{sl:.5f}</b>

🎯 TP1 : <b>{tp1:.5f}</b>
🎯 TP2 : <b>{tp2:.5f}</b>

📊 Trend H1 : {trend_h1}
📊 Trend H4 : {trend_h4}

🔍 Divergence : {divergence}

⭐ Score : {score}/100
"""

    return message