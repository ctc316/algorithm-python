class Solution:
    """
    @param n: the money of you
    @param prices: the price of rice[i]
    @param weight: the weight of rice[i]
    @param amounts: the amount of rice[i]
    @return: the maximum weight
    """
    def backPackVII(self, n, prices, weight, amounts):
        dp = [0 for _ in range(n + 1)]
        for i in range(len(prices)):
            for j in range(1, amounts[i] + 1): # 多件相同物品，都跑一次
                for k in range(n, prices[i] - 1, -1):
                    dp[k] =  max(dp[k], dp[k - prices[i]] + weight[i])

        return dp[n]