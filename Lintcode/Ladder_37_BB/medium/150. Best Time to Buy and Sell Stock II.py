class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        '''
            sell  own
        2    0    -2
        1    0    -1
        2    1    -1
        0    1     1
        1    2     1
        '''
        sell = 0
        own = float("-inf")
        for p in prices:
            sell = max(sell, p + own)
            own = max(own, sell - p)

        return sell