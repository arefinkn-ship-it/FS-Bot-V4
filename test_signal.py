import MetaTrader5 as mt5

from data_fetcher_mt5 import (
    initialize_mt5,
    shutdown_mt5,
    get_h1_data,
    get_h4_data
)

from indicators import add_indicators

from pivot_engine import (
    find_pivots,
    build_pivot_history
)

from fib_engine import (
    calculate_fib_levels
)

from trend_filter import (
    get_market_trend
)

from divergence_engine import (
    detect_divergence
)

from scoring_engine import (
    calculate_score
)

from signal_engine import (
    generate_signal,
    signal_strength
)

initialize_mt5()

df_h1 = get_h1_data(
    "XAUUSD",
    1000
)

df_h4 = get_h4_data(
    "XAUUSD",
    1000
)

df_h1 = add_indicators(df_h1)
df_h4 = add_indicators(df_h4)

df_h1 = find_pivots(df_h1)
df_h1 = build_pivot_history(df_h1)
df_h1 = calculate_fib_levels(df_h1)

trend_h1 = get_market_trend(df_h1)
trend_h4 = get_market_trend(df_h4)

divergence = detect_divergence(df_h1)

score = calculate_score(
    df_h1,
    trend_h1,
    trend_h4,
    divergence
)

signal = generate_signal(
    trend_h1,
    trend_h4,
    divergence,
    score
)

grade = signal_strength(score)

print()
print("Trend H1:", trend_h1)
print("Trend H4:", trend_h4)
print("Divergence:", divergence)
print("Score:", score)
print("Grade:", grade)
print("Signal:", signal)
print()

shutdown_mt5()