from binance.client import Client
from src.helpers import transform_kline_data
import dotenv
import os

dotenv.load_dotenv()


def get_binance_client():
    return Client(os.getenv("BINANCE_API_KEY"), os.getenv("BINANCE_API_SECRET"))


def get_list_of_symbols():
    client = get_binance_client()
    exchange_info = client.get_exchange_info()
    if 'symbols' not in exchange_info:
        return []

    symbols = exchange_info['symbols']
    # remove anything that isn't a USDT pair
    symbols = [symbol for symbol in symbols if 'USDT' in symbol['symbol']]
    return symbols


def get_hourly_data(symbol, start_date, end_date, limit=500):
    client = get_binance_client()
    kl = client.get_historical_klines(
        symbol=f"{symbol}USDT",
        interval=Client.KLINE_INTERVAL_1HOUR,
        start_str=start_date,
        end_str=end_date,
        limit=limit)

    return transform_kline_data(kl)
