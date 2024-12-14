import pandas as pd


def calculate_exponential_moving_average(data, window):
    if not data or window <= 0 or window > len(data):
        raise ValueError("Invalid input data or window size")

    series = pd.Series(data)
    ema = series.ewm(span=window, adjust=False).mean().tolist()
    return ema
