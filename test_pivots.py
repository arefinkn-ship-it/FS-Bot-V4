from data_fetcher_mt5 import (
    initialize_mt5,
    shutdown_mt5,
    get_h1_data
)

from indicators import add_indicators

from pivot_engine import (
    find_pivots,
    build_pivot_history
)

initialize_mt5()

df = get_h1_data(
    "XAUUSD",
    500
)

df = add_indicators(df)

df = find_pivots(df)

df = build_pivot_history(df)

print()

print(
    df[
        [
            "high",
            "low",
            "pivot_high",
            "pivot_low",
            "lastPH",
            "prevPH",
            "lastPL",
            "prevPL"
        ]
    ].tail(20)
)

print()

shutdown_mt5()