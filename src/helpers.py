import pandas as pd


def transform_data(raw_data):
    structured_data = []
    for entry in raw_data:
        structured_data.append({
            "timestamp": entry[0],
            "open": float(entry[1]),
            "high": float(entry[2]),
            "low": float(entry[3]),
            "close": float(entry[4]),
            "volume": float(entry[5]),
            "close_time": entry[6],
            "quote_asset_volume": float(entry[7]),
            "number_of_trades": entry[8],
            "taker_buy_base_asset_volume": float(entry[9]),
            "taker_buy_quote_asset_volume": float(entry[10]),
            "ignore": entry[11]
        })
    return structured_data


def transform_data_to_dataframe(data):
    if data is None:
        raise ValueError("Invalid input data")

    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df


def transform_kline_data(data):
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time',
                                     'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume',
                                     'taker_buy_quote_asset_volume', 'ignore'])

    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    df['close'] = df['close'].astype(float)
    df['open'] = df['open'].astype(float)
    df['high'] = df['high'].astype(float)
    df['low'] = df['low'].astype(float)
    df['volume'] = df['volume'].astype(float)

    return df
