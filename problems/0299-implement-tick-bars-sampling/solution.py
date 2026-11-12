def tick_bars(ticks: list, bar_size: int) -> list:
    """
    Sample tick data into tick bars.
    
    Args:
        ticks: List of tuples (timestamp, price, volume) representing individual trades
        bar_size: Number of ticks per bar
    
    Returns:
        List of dictionaries with keys: 'timestamp', 'open', 'high', 'low', 'close', 'volume'
    """
    if not ticks or bar_size <= 0:
        return []

    bars = []

    # Process only complete groups
    for i in range(0, len(ticks) - bar_size + 1, bar_size):

        group = ticks[i:i + bar_size]

        prices = [tick[1] for tick in group]
        volumes = [tick[2] for tick in group]

        bar = {
            "timestamp": group[-1][0],
            "open": round(prices[0], 2),
            "high": round(max(prices), 2),
            "low": round(min(prices), 2),
            "close": round(prices[-1], 2),
            "volume": round(sum(volumes), 2)
        }

        bars.append(bar)

    return bars