import pandas as pd


def detect_swings(df):
    """
    Detect market swings from pivot points.

    Requires:
        pivot_high
        pivot_low
        high
        low
    """

    df = df.copy()

    df["swing"] = None

    highs = df[df["pivot_high"]]
    lows = df[df["pivot_low"]]

    # ----- Higher High / Lower High -----

    previous_high = None

    for idx, row in highs.iterrows():

        if previous_high is None:
            previous_high = row["high"]
            continue

        if row["high"] > previous_high:
            df.loc[idx, "swing"] = "HH"
        else:
            df.loc[idx, "swing"] = "LH"

        previous_high = row["high"]

    # ----- Higher Low / Lower Low -----

    previous_low = None

    for idx, row in lows.iterrows():

        if previous_low is None:
            previous_low = row["low"]
            continue

        if row["low"] > previous_low:
            df.loc[idx, "swing"] = "HL"
        else:
            df.loc[idx, "swing"] = "LL"

        previous_low = row["low"]

    return df


def latest_structure(df):
    """
    Return latest market structure.
    """

    swings = df[df["swing"].notna()]

    if len(swings) < 4:

        return {
            "trend": "UNKNOWN",
            "strength": 0
        }

    last = swings.tail(4)["swing"].tolist()

    # Uptrend

    if last == ["HH", "HL", "HH", "HL"]:

        return {

            "trend": "UPTREND",

            "strength": 95

        }

    # Downtrend

    if last == ["LH", "LL", "LH", "LL"]:

        return {

            "trend": "DOWNTREND",

            "strength": 95

        }

    # Early reversal

    if "HH" in last and "LL" in last:

        return {

            "trend": "REVERSAL",

            "strength": 70

        }

    return {

        "trend": "RANGE",

        "strength": 40

    }