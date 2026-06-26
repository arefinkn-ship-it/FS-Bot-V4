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

from fib_engine import (
    calculate_fib_levels
)

initialize_mt5()

df = get_h1_data(
    "XAUUSD",
    500
)

df = add_indicators(df)

df = find_pivots(df)

df = build_pivot_history(df)

df = calculate_fib_levels(df)

print()

print(
    df[
        [
            "close",
            "fib_382",
            "fib_618",
            "fib_786",
            "fib_886",
            "fib_1272",
            "fib_1414",
            "fib_1618"
        ]
    ].tail(10)
)

print()

shutdown_mt5()