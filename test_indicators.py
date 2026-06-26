from data_fetcher_mt5 import (
    initialize_mt5,
    shutdown_mt5,
    get_h1_data
)

from indicators import add_indicators

initialize_mt5()

df = get_h1_data(
    "XAUUSD",
    300
)

df = add_indicators(df)

print(df.tail())

shutdown_mt5()