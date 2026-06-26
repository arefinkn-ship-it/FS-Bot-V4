import pandas as pd


def detect_market_structure(df):
    """
    Detect market structure from confirmed swing points.

    Requires:
        pivot_high
        pivot_low
        high
        low
    """

    highs = df[df["pivot_high"]]
    lows = df[df["pivot_low"]]

    if len(highs) < 2 or len(lows) < 2:
        return {
            "structure": "UNKNOWN",
            "strength": 0
        }

    last_high = highs.iloc[-1]["high"]
    prev_high = highs.iloc[-2]["high"]

    last_low = lows.iloc[-1]["low"]
    prev_low = lows.iloc[-2]["low"]

    higher_high = last_high > prev_high
    lower_high = last_high < prev_high

    higher_low = last_low > prev_low
    lower_low = last_low < prev_low

    # Strong uptrend
    if higher_high and higher_low:

        strength = 60

        if (last_high - prev_high) > (last_low - prev_low):
            strength += 20

        return {
            "structure": "UPTREND",
            "strength": strength,
            "last_high": last_high,
            "last_low": last_low
        }

    # Strong downtrend
    if lower_high and lower_low:

        strength = 60

        if (prev_low - last_low) > (prev_high - last_high):
            strength += 20

        return {
            "structure": "DOWNTREND",
            "strength": strength,
            "last_high": last_high,
            "last_low": last_low
        }

    # Mixed conditions
    if higher_high and lower_low:

        return {
            "structure": "EXPANSION",
            "strength": 50,
            "last_high": last_high,
            "last_low": last_low
        }

    if lower_high and higher_low:

        return {
            "structure": "CONSOLIDATION",
            "strength": 40,
            "last_high": last_high,
            "last_low": last_low
        }

    return {
        "structure": "RANGE",
        "strength": 30,
        "last_high": last_high,
        "last_low": last_low
    }