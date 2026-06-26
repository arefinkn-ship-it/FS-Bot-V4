import numpy as np


FAST = [3, 5, 8, 10, 12, 15]
SLOW = [30, 35, 40, 45, 50, 60]


def gmma_alignment(df):
    """
    Returns:
        BULL
        BEAR
        MIXED
    """

    row = df.iloc[-1]

    fast = [row[f"ema{x}"] for x in FAST]
    slow = [row[f"ema{x}"] for x in SLOW]

    if min(fast) > max(slow):
        return "BULL"

    if max(fast) < min(slow):
        return "BEAR"

    return "MIXED"


def gmma_strength(df):
    """
    Returns strength 0-100
    """

    row = df.iloc[-1]

    fast = np.mean([row[f"ema{x}"] for x in FAST])
    slow = np.mean([row[f"ema{x}"] for x in SLOW])

    close = row["close"]

    distance = abs(fast - slow) / close

    score = min(distance * 10000, 100)

    return round(score)