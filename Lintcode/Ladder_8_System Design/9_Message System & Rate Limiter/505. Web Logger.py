class WebLogger:

    def __init__(self):
        self.logs = []

    """
    @param: timestamp: An integer
    @return: nothing
    """
    def hit(self, timestamp):
        self.logs.append(timestamp)

    """
    @param: timestamp: An integer
    @return: An integer
    """
    def get_hit_count_in_last_5_minutes(self, timestamp):
        from bisect import bisect_right
        pos = bisect_right(self.logs, timestamp - 300)
        return len(self.logs) - pos