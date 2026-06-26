import MetaTrader5 as mt5
import pandas as pd


def get_data(symbol, timeframe, bars=1000):
    """
    Download OHLC data from MT5

    Parameters
    ----------
    symbol : str
        MT5 symbol name

    timeframe : MT5 timeframe
        Example:
        mt5.TIMEFRAME_H1
        mt5.TIMEFRAME_H4

    bars : int
        Number of candles

    Returns
    -------
    pandas.DataFrame
    """

    rates = mt5.copy_rates_from_pos(
        symbol,
        timeframe,
        0,
        bars
    )

    if rates is None:
        print(f"❌ No data returned for {symbol}")
        return pd.DataFrame()

    df = pd.DataFrame(rates)

    if df.empty:
        print(f"❌ Empty dataframe for {symbol}")
        return pd.DataFrame()

    # Convert timestamp
    df["time"] = pd.to_datetime(
        df["time"],
        unit="s"
    )

    df.set_index(
        "time",
        inplace=True
    )

    required_cols = [
        "open",
        "high",
        "low",
        "close"
    ]

    for col in required_cols:
        if col not in df.columns:
            print(
                f"❌ Missing column {col} for {symbol}"
            )
            return pd.DataFrame()

    return df


def get_h1_data(symbol, bars=1000):
    return get_data(
        symbol,
        mt5.TIMEFRAME_H1,
        bars
    )


def get_h4_data(symbol, bars=1000):
    return get_data(
        symbol,
        mt5.TIMEFRAME_H4,
        bars
    )


def check_symbol(symbol):
    """
    Verify symbol exists in MT5
    """

    info = mt5.symbol_info(symbol)

    if info is None:
        return False

    return True


def initialize_mt5():
    """
    Connect to MT5
    """

    if not mt5.initialize():
        print("❌ MT5 connection failed")
        return False

    print("✅ MT5 Connected")
    return True


def shutdown_mt5():
    """
    Close MT5 connection
    """

    mt5.shutdown()