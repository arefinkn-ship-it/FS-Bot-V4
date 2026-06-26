from trend_filter import get_market_trend
from market_structure import detect_market_structure
from divergence_engine import detect_divergence
from fib_engine import calculate_fib_levels, price_in_fib_zone
from scoring_engine import calculate_score
from signal_engine import generate_signal
from risk_manager import build_trade


def analyze_pair(df_h1, df_h4):
    """
    Complete analysis pipeline.
    Returns a trade dictionary or None.
    """

    # ----------------------------
    # Trend
    # ----------------------------

    trend_h1 = get_market_trend(df_h1)
    trend_h4 = get_market_trend(df_h4)

    # ----------------------------
    # Market Structure
    # ----------------------------

    structure = detect_market_structure(df_h1)

    # ----------------------------
    # Divergence
    # ----------------------------

    divergence = detect_divergence(df_h1)

    # ----------------------------
    # Fibonacci
    # ----------------------------

    fib = calculate_fib_levels(df_h1)

    fib_valid = price_in_fib_zone(
        df_h1.iloc[-1]["close"],
        fib
    )

    # ----------------------------
    # Score
    # ----------------------------

    score = calculate_score(
        trend_h1=trend_h1,
        trend_h4=trend_h4,
        structure=structure,
        divergence=divergence,
        fib_valid=fib_valid,
        df=df_h1
    )

    # ----------------------------
    # Signal
    # ----------------------------

    signal = generate_signal(
        trend_h1,
        trend_h4,
        structure,
        divergence,
        score
    )

    if signal is None:
        return None

    # ----------------------------
    # Risk
    # ----------------------------

    trade = build_trade(
        signal=signal,
        score=score,
        trend_h1=trend_h1,
        trend_h4=trend_h4,
        divergence=divergence,
        df=df_h1
    )

    return trade