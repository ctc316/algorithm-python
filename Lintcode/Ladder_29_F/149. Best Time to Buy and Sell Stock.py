class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        lowest = sys.maxsize
        max_profit = 0
        for p in prices:
            max_profit = max(max_profit, p - lowest)
            lowest = min(lowest, p)

        return max_profit