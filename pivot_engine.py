import numpy as np


def find_pivots(df, left=5, right=5):

    df = df.copy()

    df["pivot_high"] = False
    df["pivot_low"] = False

    for i in range(left, len(df) - right):

        current_high = df.iloc[i]["high"]
        current_low = df.iloc[i]["low"]

        high_window = df.iloc[
            i-left:i+right+1
        ]["high"]

        low_window = df.iloc[
            i-left:i+right+1
        ]["low"]

        if current_high == high_window.max():

            df.at[
                df.index[i],
                "pivot_high"
            ] = True

        if current_low == low_window.min():

            df.at[
                df.index[i],
                "pivot_low"
            ] = True

    return df
def build_pivot_history(df):

    df = df.copy()

    df["lastPH"] = np.nan
    df["prevPH"] = np.nan

    df["lastPL"] = np.nan
    df["prevPL"] = np.nan

    df["rsiAtPH"] = np.nan
    df["rsiAtPrevPH"] = np.nan

    df["rsiAtPL"] = np.nan
    df["rsiAtPrevPL"] = np.nan

    lastPH = np.nan
    prevPH = np.nan

    lastPL = np.nan
    prevPL = np.nan

    rsiAtPH = np.nan
    rsiAtPrevPH = np.nan

    rsiAtPL = np.nan
    rsiAtPrevPL = np.nan

    for i in range(len(df)):

        if df.iloc[i]["pivot_high"]:

            prevPH = lastPH
            lastPH = df.iloc[i]["high"]

            rsiAtPrevPH = rsiAtPH
            rsiAtPH = df.iloc[i]["rsi"]

        if df.iloc[i]["pivot_low"]:

            prevPL = lastPL
            lastPL = df.iloc[i]["low"]

            rsiAtPrevPL = rsiAtPL
            rsiAtPL = df.iloc[i]["rsi"]

        idx = df.index[i]

        df.at[idx, "lastPH"] = lastPH
        df.at[idx, "prevPH"] = prevPH

        df.at[idx, "lastPL"] = lastPL
        df.at[idx, "prevPL"] = prevPL

        df.at[idx, "rsiAtPH"] = rsiAtPH
        df.at[idx, "rsiAtPrevPH"] = rsiAtPrevPH

        df.at[idx, "rsiAtPL"] = rsiAtPL
        df.at[idx, "rsiAtPrevPL"] = rsiAtPrevPL

    return df