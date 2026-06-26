import MetaTrader5 as mt5

from data_fetcher_mt5 import get_data
from indicators import add_indicators
from pivot_engine import find_pivots
from market_structure import detect_market_structure


PAIR = "XAUUSD"

mt5.initialize()

df = get_data(
    PAIR,
    mt5.TIMEFRAME_H1,
    500
)

df = add_indicators(df)

df = find_pivots(df)

result = detect_market_structure(df)

print(result)

mt5.shutdown()