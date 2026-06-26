from telegram_alert import (
    build_signal_message,
    send_telegram
)

msg = build_signal_message(
    pair="XAUUSD",
    signal="SELL",
    grade="A",
    score=88,
    entry=3986.08,
    sl=4020.34,
    tp1=3951.81,
    tp2=3917.55,
    trend_h1="BEAR",
    trend_h4="BEAR",
    divergence="HIDDEN_BEAR"
)

send_telegram(msg)