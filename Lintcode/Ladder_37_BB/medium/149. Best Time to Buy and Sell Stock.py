class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        lowest_p = float("Inf")
        max_profit = 0
        for p in prices:
            lowest_p = min(lowest_p, p)
            max_profit = max(max_profit, p - lowest_p)

        return max_profit