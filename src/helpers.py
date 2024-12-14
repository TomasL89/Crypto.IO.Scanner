# tests/helpers.py

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



