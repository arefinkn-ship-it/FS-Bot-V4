from data_fetcher_mt5 import initialize_mt5
from data_fetcher_mt5 import get_h1_data
from data_fetcher_mt5 import shutdown_mt5

initialize_mt5()

df = get_h1_data("XAUUSD", 10)

print(df.tail())

shutdown_mt5()