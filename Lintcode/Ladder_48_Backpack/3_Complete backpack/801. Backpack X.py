class Solution:
    """
    @param n: the money you have
    @return: the minimum money you have to give
    """
    def backPackX(self, n):
        yuans = [150, 250, 350]
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        for yuan in yuans:
            for i in range(yuan, n + 1):
                dp[i] = dp[i] or dp[i - yuan]

        for i in range(n, -1, -1):
            if dp[i]:
                return n - i

        return n