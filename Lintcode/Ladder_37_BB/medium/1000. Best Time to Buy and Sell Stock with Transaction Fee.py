class Solution:
    """
    @param prices: a list of integers
    @param fee: a integer
    @return: return a integer
    """
    def maxProfit(self, prices, fee):
        '''
            earned(sell)   own
        1     0      -1
        3     0      -1
        2     0      -1
        8     5      -1       
        4     5       1
        9     8       1
        '''
        sell = 0;
        own = -prices[0];
        for i in range(1, len(prices)):
            sell = max(sell, own + prices[i] - fee);
            own = max(own, sell - prices[i]);
            
        return sell;