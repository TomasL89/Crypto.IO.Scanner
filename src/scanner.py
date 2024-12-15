from datetime import datetime
from src.technical_analysis import calculate_exponential_moving_average


def scan_for_buy_signals(data):
    if data is None:
        raise ValueError("Invalid input data")

    close_data = data['close'].tolist()
    ema_50 = calculate_exponential_moving_average(close_data, 50)
    ema_200 = calculate_exponential_moving_average(close_data, 200)

    # buy signal is when the close is below the 50 and 200 day moving averages.
    # Each point and the distance from the 50 and 200 should be returned in a list
    buy_signals = []

    for i in range(len(data)):
        close = float(data['close'].iloc[i])
        ema_50_val = float(ema_50[i])
        ema_200_val = float(ema_200[i])
        close_time = data['close_time'].iloc[i]

        if close < ema_50_val and close < ema_200_val:
            timestamp = datetime.fromtimestamp(close_time / 1000).strftime('%Y-%m-%d %H:%M:%S')

            buy_signals.append({
                'epoch_time': int(close_time),
                'timestamp': timestamp,
                'close': close,
                'ema_50': ema_50_val,
                'ema_200': ema_200_val,
                'distance_from_50': ema_50_val - close,
                'distance_from_200': ema_200_val - close
            })

    return buy_signals
