from broker_data import get_hourly_data, get_list_of_symbols
from db import add_to_watchlist
from datetime import datetime
from datetime import timedelta
import os
import schedule
from scanner import scan_for_buy_signals
import time

symbols = get_list_of_symbols()


def scan_job():
    job_sw_start = time.time()
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

            if buy_signals:
                buy_signal = {
                    "symbol": symbol,
                    "buy_signals": buy_signals
                }
                add_to_watchlist(buy_signal)

            print(f"Scanning {symbol} took {time.time() - sw_start} seconds")
        except ValueError as e:
            print(f"Error scanning {symbol}: {e}")
    print(f"Job took {time.time() - job_sw_start} seconds\n")


scan_job()
schedule.every().hour.do(scan_job)

while True:
    schedule.run_pending()
    time.sleep(1)
