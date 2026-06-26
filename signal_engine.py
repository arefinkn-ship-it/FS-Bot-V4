from scoring_engine import grade_signal


def generate_signal(
    trend_h1,
    trend_h4,
    structure,
    divergence,
    score
):
    """
    Generates BUY/SELL signal.

    Returns:
        BUY
        SELL
        None
    """

    grade = grade_signal(score)

    # -----------------------------
    # BUY
    # -----------------------------
    if (
        trend_h1 == "BULL"
        and trend_h4 == "BULL"
        and structure["structure"] in [
            "UPTREND",
            "CONSOLIDATION"
        ]
        and divergence in [
            "REGULAR_BULL",
            "HIDDEN_BULL",
            "EQUAL_BULL"
        ]
        and score >= 70
    ):
        return "BUY"

    # -----------------------------
    # SELL
    # -----------------------------
    if (
        trend_h1 == "BEAR"
        and trend_h4 == "BEAR"
        and structure["structure"] in [
            "DOWNTREND",
            "CONSOLIDATION"
        ]
        and divergence in [
            "REGULAR_BEAR",
            "HIDDEN_BEAR",
            "EQUAL_BEAR"
        ]
        and score >= 70
    ):
        return "SELL"

    return None