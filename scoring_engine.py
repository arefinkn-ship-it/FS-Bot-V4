def calculate_score(
    trend_h1,
    trend_h4,
    structure,
    divergence,
    fib_valid,
    df
):
    score = 0

    # -------------------------
    # H4 Trend
    # -------------------------
    if trend_h4 in ["BULL", "BEAR"]:
        score += 20

    # -------------------------
    # H1 Trend agrees with H4
    # -------------------------
    if trend_h1 == trend_h4:
        score += 20

    # -------------------------
    # Market Structure
    # -------------------------
    if structure["structure"] == "UPTREND":
        score += 15

    elif structure["structure"] == "DOWNTREND":
        score += 15

    elif structure["structure"] == "CONSOLIDATION":
        score += 8

    # -------------------------
    # Divergence
    # -------------------------
    if divergence in [
        "REGULAR_BULL",
        "REGULAR_BEAR"
    ]:
        score += 20

    elif divergence in [
        "HIDDEN_BULL",
        "HIDDEN_BEAR"
    ]:
        score += 15

    elif divergence in [
        "EQUAL_BULL",
        "EQUAL_BEAR"
    ]:
        score += 10

    # -------------------------
    # Fibonacci
    # -------------------------
    if fib_valid:
        score += 10

    # -------------------------
    # ATR Filter
    # -------------------------
    atr = float(df.iloc[-1]["atr"])
    close = float(df.iloc[-1]["close"])

    atr_percent = atr / close

    if 0.002 <= atr_percent <= 0.02:
        score += 5

    return min(score, 100)


def grade_signal(score):

    if score >= 95:
        return "Institutional"

    if score >= 90:
        return "A+"

    if score >= 85:
        return "A"

    if score >= 80:
        return "B+"

    if score >= 70:
        return "B"

    return "IGNORE"