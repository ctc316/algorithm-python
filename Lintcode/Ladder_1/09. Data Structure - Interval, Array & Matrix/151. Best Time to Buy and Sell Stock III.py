class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0

        '''
            [2,1,4,5,2,9,7]
            i = 0, lc=[0, 0, 0], gb=[0, 0, 0]
            i = 1, lc=[0, 0, 0], gb=[0, 0, 0]
            i = 2, lc=[0, 3, 3], gb=[0, 3, 3]
            i = 3, lc=[0, 4, 4], gb=[0, 4, 4]
            i = 4, lc=[0, 1, 4], gb=[0, 4, 4]
            i = 5, ...
        '''


        # https://blog.csdn.net/linhuanmars/article/details/23236995
        # 当前到达第i天，最多可进行j次交易，并且最后一次交易在当天卖出的最好的利润是多少
        # local[i][j] = max(global[i - 1][j - 1] + max(diff, 0), local[i - 1][j] + diff)
        # 当前到达第i天可以最多进行j次交易，最好的利润是多少
        # global[i][j] = max(local[i][j], global[i - 1][j])

        # 兩次交易，可用一次交易取代 1,3,2,4,5 -> 1~5 = 1~4,4~5

        k = 2

        # records of last day's max profits for transaction times, 0, 1, 2
        localMax = [0 for _ in range(k + 1)]
        globalMax = [0 for _ in range(k + 1)]

        for i in range(n - 1):
            diff = prices[i + 1] - prices[i]
            for j in range(k, 0, -1):
                localMax[j] = max(globalMax[j - 1] + max(diff, 0), localMax[j] + diff)
                globalMax[j] = max(localMax[j], globalMax[j])

            print(localMax, globalMax)

        return globalMax[k]