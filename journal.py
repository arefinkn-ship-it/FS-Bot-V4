import os
import pandas as pd
from datetime import datetime

FILE_NAME = "trade_journal.csv"


def initialize_journal():

    if os.path.exists(FILE_NAME):
        return

    df = pd.DataFrame(columns=[

        "Time",

        "Pair",

        "Signal",

        "Grade",

        "Score",

        "Entry",

        "SL",

        "TP1",

        "TP2",

        "Trend_H1",

        "Trend_H4",

        "Divergence"

    ])

    df.to_csv(FILE_NAME, index=False)


def log_trade(pair, trade):

    initialize_journal()

    row = {

        "Time": datetime.now(),

        "Pair": pair,

        "Signal": trade["signal"],

        "Grade": trade["grade"],

        "Score": trade["score"],

        "Entry": trade["entry"],

        "SL": trade["sl"],

        "TP1": trade["tp1"],

        "TP2": trade["tp2"],

        "Trend_H1": trade["trend_h1"],

        "Trend_H4": trade["trend_h4"],

        "Divergence": trade["divergence"]

    }

    df = pd.read_csv(FILE_NAME)

    df = pd.concat(

        [

            df,

            pd.DataFrame([row])

        ],

        ignore_index=True

    )

    df.to_csv(FILE_NAME, index=False)