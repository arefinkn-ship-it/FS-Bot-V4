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

from divergence_engine import (
    detect_divergence,
    divergence_score
)

initialize_mt5()

df = get_h1_data(
    "XAUUSD",
    1000
)

df = add_indicators(df)

df = find_pivots(df)

df = build_pivot_history(df)

signal = detect_divergence(df)

print()

print("Divergence:", signal)

print(
    "Score:",
    divergence_score(signal)
)

print()

shutdown_mt5()