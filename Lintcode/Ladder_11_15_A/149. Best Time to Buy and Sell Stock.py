class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        lowest_p = float("Inf")
        max_profit = 0
        for p in prices:
            max_profit = max(max_profit, p - lowest)
            lowest_p = min(lowest, p)

        return max_profit