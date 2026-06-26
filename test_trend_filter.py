from data_fetcher_mt5 import (
    initialize_mt5,
    shutdown_mt5,
    get_h1_data
)

from indicators import add_indicators
from trend_filter import get_market_trend

initialize_mt5()

df = get_h1_data(
    "XAUUSD",
    300
)

df = add_indicators(df)

trend = get_market_trend(df)

print()
print("Trend:", trend)
print()

shutdown_mt5()