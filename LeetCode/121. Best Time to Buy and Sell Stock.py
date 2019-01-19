class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        n = len(prices)
        if n < 2:
            return 0
        
        max_profit = 0
        min_price = prices[0]
        
        for i in range(1, n):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_price)

        return max_profit