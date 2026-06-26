from data_fetcher_mt5 import (
    initialize_mt5,
    shutdown_mt5,
    get_h1_data
)

from indicators import add_indicators
from gmma_engine import (
    get_gmma_state,
    get_gmma_score
)

initialize_mt5()

df = get_h1_data(
    "XAUUSD",
    300
)

df = add_indicators(df)

print()

print(
    "GMMA State:",
    get_gmma_state(df)
)

print(
    "GMMA Score:",
    get_gmma_score(df)
)

print()

shutdown_mt5()