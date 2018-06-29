class Solution:
    """
    @param m: the number of eggs
    @param n: the number of floors
    @return: the number of drops in the worst case
    """
    def dropEggs2(self, m, n):
        # dp[i][j]: i顆蛋 共j層 的次數
        dp = [[sys.maxsize for _ in range(n + 1)] for _ in range(m + 1)]

        # init: 只有一層樓的，需丟一次，零層樓丟零次
        for i in range(1, m + 1):
            dp[i][1] = 1
            dp[i][0] = 0

        # init: 只有一顆蛋的話，都從1樓開始丟
        for j in range(1, n + 1):
            dp[1][j] = j

        for i in range(2, m + 1):
            for j in range(2, n + 1):
                # 1 ~ j 樓
                for k in range(1, j + 1):
                    # 1 + dp[i-1][k-1] 这是如果碎了的话，用了多少次
                    # 1 + dp[i][j-k], 这是如果没碎用了多少次
                    # min是看当前需要的次数和即将要比较的drop egg的楼层所generate的wcs的次数的比较。
                    # max是因为要看worst case scenario, 所以看在这层楼扔蛋碎了和没碎所需要次数的最大值。
                    dp[i][j] = min(dp[i][j], 1 + max(dp[i - 1][k - 1], dp[i][j - k]))

        return dp[m][n]