from datetime import datetime
from src.helpers import transform_data_to_dataframe
from src.technical_analysis import calculate_exponential_moving_average


def scan_for_buy_signals(data):
    if data is None:
        raise ValueError("Invalid input data")

    data = transform_data_to_dataframe(data)
    close_data = data['close'].tolist()
    ema_50 = calculate_exponential_moving_average(close_data, 50)
    ema_200 = calculate_exponential_moving_average(close_data, 200)

    # buy signal is when the close is below the 50 and 200 day moving averages.
    # Each point and the distance from the 50 and 200 should be returned in a list
    buy_signals = []

    for i in range(len(data)):
        if data['close'][i] < ema_50[i] and data['close'][i] < ema_200[i]:
            timestamp = datetime.fromtimestamp(data['close_time'][i] / 1000).strftime('%Y-%m-%d %H:%M:%S')

            buy_signals.append({
                'epoch_time': data['close_time'][i],
                'timestamp': timestamp,
                'close': float(data['close'][i]),
                'ema_50': float(ema_50[i]),
                'ema_200': float(ema_200[i]),
                'distance_from_50': float(ema_50[i] - data['close'][i]),
                'distance_from_200': float(ema_200[i] - data['close'][i])
            })

    return buy_signals
