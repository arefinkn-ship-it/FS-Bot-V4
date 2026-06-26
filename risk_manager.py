import numpy as np
from scoring_engine import grade_signal


ATR_MULTIPLIER = 1.5
TP1_RR = 1.0
TP2_RR = 2.0
TP3_RR = 3.0


def calculate_position(entry, sl):
    risk = abs(entry - sl)

    if risk == 0:
        risk = 0.00001

    return risk


def long_levels(entry, atr):

    sl = entry - (atr * ATR_MULTIPLIER)

    risk = calculate_position(entry, sl)

    tp1 = entry + (risk * TP1_RR)
    tp2 = entry + (risk * TP2_RR)
    tp3 = entry + (risk * TP3_RR)

    return sl, tp1, tp2, tp3


def short_levels(entry, atr):

    sl = entry + (atr * ATR_MULTIPLIER)

    risk = calculate_position(entry, sl)

    tp1 = entry - (risk * TP1_RR)
    tp2 = entry - (risk * TP2_RR)
    tp3 = entry - (risk * TP3_RR)

    return sl, tp1, tp2, tp3


def build_trade(
    signal,
    score,
    trend_h1,
    trend_h4,
    divergence,
    df
):
    """
    Build complete trade dictionary.
    """

    row = df.iloc[-1]

    entry = float(row["close"])
    atr = float(row["atr"])

    if signal == "BUY":

        sl, tp1, tp2, tp3 = long_levels(entry, atr)

    elif signal == "SELL":

        sl, tp1, tp2, tp3 = short_levels(entry, atr)

    else:

        return None

    risk = abs(entry - sl)

    trade = {

        "signal": signal,

        "grade": grade_signal(score),

        "score": score,

        "entry": round(entry, 5),

        "sl": round(sl, 5),

        "tp1": round(tp1, 5),

        "tp2": round(tp2, 5),

        "tp3": round(tp3, 5),

        "risk": round(risk, 5),

        "rr1": "1:1",

        "rr2": "1:2",

        "rr3": "1:3",

        "trend_h1": trend_h1,

        "trend_h4": trend_h4,

        "divergence": divergence,

        "atr": round(atr, 5)

    }

    return trade