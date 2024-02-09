# position analysis
## 1. price

## 1.1 price / max_length
def get_price_max_length_position(prices, max_length):
    positions_list = list()
    for idx in range(1, len(prices) + 1):
        _prices = prices.iloc[max(0, idx - max_length) : idx]
        _prices_arr = _prices.apply(lambda x: [x]).values
        _positions = _prices_arr
        positions = np.concatenate(_positions)
        positions_list.append([list(positions)])
    position_df = pd.DataFrame(positions_list, columns=["positions"])
    return position_df


max_length = 90
position_df = get_price_max_length_position(prices, max_length)
position_df

## 1.2 price / max_length / time_weighted


def get_price_max_length_time_wegithed_position(prices, max_length):
    positions_list = list()
    for idx in range(1, len(prices) + 1):
        _prices = prices.iloc[max(0, idx - max_length) : idx]
        _prices_arr = _prices.apply(lambda x: [x]).values

        _time_weights = np.arange(1, len(_prices) + 1)

        _positions = _prices_arr * _time_weights
        positions = np.concatenate(_positions)
        positions_list.append([positions])
    position_df = pd.DataFrame(positions_list, columns=["positions"])
    return position_df


max_length = 90
position_df = get_price_max_length_time_wegithed_position(prices, max_length)
position_df

## 1.3 price / volume / max_length
def get_price_volume_max_length_position(prices, volumes, max_length):
    positions_list = list()
    for idx in range(1, len(prices) + 1):
        _prices = prices.iloc[max(0, idx - max_length) : idx]
        _prices_arr = _prices.apply(lambda x: [x]).values

        _volumes = volumes.iloc[max(0, idx - max_length) : idx]
        _normalized_volumes = (_volumes * max_length) / _volumes.sum()
        _normalized_volume_weights = _normalized_volumes.apply(
            lambda x: int(round(x))
        ).values
        _positions = _prices_arr * _normalized_volume_weights
        positions = np.concatenate(_positions)
        positions_list.append([positions])
    position_df = pd.DataFrame(positions_list, columns=["positions"])
    return position_df


position_df = get_price_volume_max_length_position(prices, volumes, max_length)
position_df

## 1.4 price / volume / max_length / time_weighted
def get_price_volume_max_length_time_weighted_position(
    prices, volumes, max_length
):
    positions_list = list()
    for idx in range(1, len(prices) + 1):
        _prices = prices.iloc[max(0, idx - max_length) : idx]
        _prices_arr = _prices.apply(lambda x: [x]).values

        _volumes = volumes.iloc[max(0, idx - max_length) : idx]
        _normalized_volumes = (_volumes * max_length) / _volumes.sum()
        _normalized_volume_weights = _normalized_volumes.apply(
            lambda x: int(round(x))
        ).values

        _time_weights = np.arange(1, len(_prices) + 1)

        volume_time_weights = _normalized_volume_weights * _time_weights

        _positions = _prices_arr * volume_time_weights
        positions = np.concatenate(_positions)
        positions_list.append([positions])
    position_df = pd.DataFrame(positions_list, columns=["positions"])
    return position_df

position_df = get_price_volume_max_length_time_weighted_position(prices, volumes, max_length)
position_df

