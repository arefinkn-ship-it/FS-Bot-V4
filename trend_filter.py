def get_market_trend(df):

    row = df.iloc[-1]

    close = row["close"]
    cloud_top = row["cloud_top"]
    cloud_bottom = row["cloud_bottom"]

    if close > cloud_top:
        return "BULL"

    if close < cloud_bottom:
        return "BEAR"

    return "RANGE"


def trend_agreement(h1_trend, h4_trend):

    if h1_trend == "BULL" and h4_trend == "BULL":
        return True

    if h1_trend == "BEAR" and h4_trend == "BEAR":
        return True

    return False