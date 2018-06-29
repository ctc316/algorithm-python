# Time: O(n)
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0

        minBuy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - minBuy)
            minBuy = min(minBuy, prices[i])

        return profit