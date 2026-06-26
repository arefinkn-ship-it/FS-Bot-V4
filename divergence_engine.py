def detect_divergence(df):
    """
    Returns:

    REGULAR_BULL
    HIDDEN_BULL
    EQUAL_BULL

    REGULAR_BEAR
    HIDDEN_BEAR
    EQUAL_BEAR

    None
    """

    lows = df[df["pivot_low"]]

    highs = df[df["pivot_high"]]

    # ------------------------

    if len(lows) >= 2:

        prev = lows.iloc[-2]

        curr = lows.iloc[-1]

        if curr["low"] < prev["low"] and curr["rsi"] > prev["rsi"]:

            return "REGULAR_BULL"

        if curr["low"] > prev["low"] and curr["rsi"] < prev["rsi"]:

            return "HIDDEN_BULL"

        if abs(curr["low"] - prev["low"]) / prev["low"] < 0.001:

            if curr["rsi"] < prev["rsi"]:

                return "EQUAL_BULL"

    # ------------------------

    if len(highs) >= 2:

        prev = highs.iloc[-2]

        curr = highs.iloc[-1]

        if curr["high"] > prev["high"] and curr["rsi"] < prev["rsi"]:

            return "REGULAR_BEAR"

        if curr["high"] < prev["high"] and curr["rsi"] > prev["rsi"]:

            return "HIDDEN_BEAR"

        if abs(curr["high"] - prev["high"]) / prev["high"] < 0.001:

            if curr["rsi"] > prev["rsi"]:

                return "EQUAL_BEAR"

    return None