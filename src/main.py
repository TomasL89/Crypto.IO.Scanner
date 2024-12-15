from broker_data import get_hourly_data, get_list_of_symbols
from db import add_to_watchlist
from datetime import datetime
from datetime import timedelta
import os
import schedule
from scanner import scan_for_buy_signals
import time

from src.db import upsert_to_watchlist

symbols = get_list_of_symbols()
buy_signal_timeframe = 24


def scan_job():
    job_sw_start = time.time()
    symbols_found = 0
    for symbol in symbols:
        try:
            sw_start = time.time()
            end_time = datetime.now()
            start_time = end_time - timedelta(days=42)
            data = get_hourly_data(
                symbol=symbol,
                start_date=str(start_time),
                end_date=str(end_time),
                limit=1000)

            buy_signals = scan_for_buy_signals(data)

            # remove any buy signals that are not within the last 24 hours
            buy_signals = [signal for signal in buy_signals
                           if datetime.strptime(signal['timestamp'], '%Y-%m-%d %H:%M:%S') > end_time - timedelta(hours=buy_signal_timeframe)]

            if buy_signals:
                buy_signal = {
                    "symbol": symbol,
                    "buy_signals": buy_signals
                }
                upsert_to_watchlist(buy_signal)
                symbols_found += 1

            print(f"Scanning {symbol} took {time.time() - sw_start} seconds")
        except ValueError as e:
            print(f"Error scanning {symbol}: {e}")
    print(f"Job took {time.time() - job_sw_start} seconds. Found {symbols_found} symbols\n")


scan_job()
schedule.every().hour.do(scan_job)

while True:
    schedule.run_pending()
    time.sleep(1)
