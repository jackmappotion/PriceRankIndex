# position analysis
## 1. price
from collections import deque

## 1.1 price / max_length
def get_price_max_length_position(prices, max_length):
    positions_list = list()
    for idx in range(1, len(prices) + 1):
        _prices = prices.iloc[max(0, idx - max_length) : idx]
        _positions = _prices.apply(lambda x: [x]).values
        positions = np.concatenate(_positions)
        positions_list.append([list(positions)])
    position_df = pd.DataFrame(positions_list, columns=["positions"])
    return position_df


max_length = 90
position_df = get_price_max_length_position(prices, max_length)

## 1.2 price / max_length / time_weighted

def get_price_max_length_time_wegithed_position(prices, max_length):
    positions_list = list()
    for idx in range(1, len(prices) + 1):
        _prices = prices.iloc[max(0, idx - max_length) : idx]
        _positions = _prices.apply(lambda x: [x]).values * np.arange(
            1, len(_prices) + 1
        )
        positions = np.concatenate(_positions)
        positions_list.append([positions])
    position_df = pd.DataFrame(positions_list, columns=["positions"])
    return position_df


max_length = 90
position_df = get_price_max_length_time_wegithed_position(prices, max_length)

