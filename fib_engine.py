def calculate_fib_levels(df):
    """
    Calculate latest Fibonacci levels
    """

    swing_high = df["high"].tail(200).max()
    swing_low = df["low"].tail(200).min()

    diff = swing_high - swing_low

    return {

        "high": swing_high,

        "low": swing_low,

        "0.382": swing_high - diff * 0.382,

        "0.5": swing_high - diff * 0.50,

        "0.618": swing_high - diff * 0.618,

        "0.786": swing_high - diff * 0.786,

        "1.272": swing_low - diff * 0.272,

        "1.618": swing_low - diff * 0.618

    }


def price_in_fib_zone(price, fib):

    tolerance = price * 0.002

    zones = [

        fib["0.382"],

        fib["0.5"],

        fib["0.618"],

        fib["0.786"]

    ]

    for level in zones:

        if abs(price - level) <= tolerance:
            return True

    return False