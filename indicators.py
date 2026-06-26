import ta
import pandas as pd


def add_indicators(df):

    # =========================
    # RSI
    # =========================

    df["rsi"] = ta.momentum.RSIIndicator(
        close=df["close"],
        window=14
    ).rsi()

    # =========================
    # ATR
    # =========================

    df["atr"] = ta.volatility.AverageTrueRange(
        high=df["high"],
        low=df["low"],
        close=df["close"],
        window=14
    ).average_true_range()

    # =========================
    # Main EMAs
    # =========================

    df["ema13"] = ta.trend.EMAIndicator(
        close=df["close"],
        window=13
    ).ema_indicator()

    df["ema34"] = ta.trend.EMAIndicator(
        close=df["close"],
        window=34
    ).ema_indicator()

    df["ema89"] = ta.trend.EMAIndicator(
        close=df["close"],
        window=89
    ).ema_indicator()

    # =========================
    # GMMA FAST EMAs
    # =========================

    fast_periods = [
        3, 5, 8,
        10, 12, 15
    ]

    for p in fast_periods:

        df[f"ema{p}"] = ta.trend.EMAIndicator(
            close=df["close"],
            window=p
        ).ema_indicator()

    # =========================
    # GMMA SLOW EMAs
    # =========================

    slow_periods = [
        30, 35, 40,
        45, 50, 60
    ]

    for p in slow_periods:

        df[f"ema{p}"] = ta.trend.EMAIndicator(
            close=df["close"],
            window=p
        ).ema_indicator()

    # =========================
    # ICHIMOKU
    # =========================

    ichi = ta.trend.IchimokuIndicator(
        high=df["high"],
        low=df["low"],
        window1=9,
        window2=26,
        window3=52
    )

    df["tenkan"] = ichi.ichimoku_conversion_line()

    df["kijun"] = ichi.ichimoku_base_line()

    df["ssa"] = ichi.ichimoku_a()

    df["ssb"] = ichi.ichimoku_b()

    # =========================
    # CHIKOU CLOUD FILTER
    # Pine Equivalent:
    # close > max(ssa[26], ssb[26])
    # =========================

    df["ssa_26"] = df["ssa"].shift(26)

    df["ssb_26"] = df["ssb"].shift(26)

    df["cloud_top"] = df[
        ["ssa_26", "ssb_26"]
    ].max(axis=1)

    df["cloud_bottom"] = df[
        ["ssa_26", "ssb_26"]
    ].min(axis=1)

    # =========================
    # ATR %
    # Useful for scoring
    # =========================

    df["atr_pct"] = (
        df["atr"] /
        df["close"]
    )

    return df