import MetaTrader5 as mt5

from data_fetcher_mt5 import get_data
from indicators import add_indicators
from pivot_engine import find_pivots

from swing_engine import (
    detect_swings,
    latest_structure
)

PAIR = "XAUUSD"

mt5.initialize()

df = get_data(
    PAIR,
    mt5.TIMEFRAME_H1,
    500
)

df = add_indicators(df)

df = find_pivots(df)

df = detect_swings(df)

print(df[df["swing"].notna()][
    ["high", "low", "swing"]
].tail(15))

print()

print(latest_structure(df))

mt5.shutdown()