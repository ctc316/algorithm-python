class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        '''
         [1,2,3,4,5,2,1,3]
          increasing:  5-1 = 5-4 + 4-3 + ....
          2
          3-1
        '''

        if len(prices) == 0:
            return 0

        total = 0
        low = high = sys.maxsize
        for p in prices:
            if p > high:
                high = p
            else:
                # sell and buy new
                total += high - low
                low = high = p

        # close deal
        total += high - low

        return total