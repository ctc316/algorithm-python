class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):

        '''
            n=3, k=2
            [0, 2, 4, ]
            1: 0, 1
            2: 00,11,01,10
            3: 011,100 + 001,110,010,101
        '''

        # Base: 第二根塗色的方式是k*k，因為第二根柱子可以和第一根一樣
        dp = [0, k, k * k]

        if n <= 2:
            return dp[n]

        # Recursion
        # 第三根柱子
        # 1) 跟前一個柱子同顏色，且與前前一個柱子不同顏色 (根據dp[-1]做變化)
        # 2) 跟前兩二根柱子都不是一个颜色。（根據dp[-2] 做變化)
        # 遞推式：dp[3] = (k - 1) * dp[1] + (k - 1) * dp[2]。
        for i in range(2, n):
            dp.append((k - 1) * (dp[-1] + dp[-2]))

        return dp[-1]