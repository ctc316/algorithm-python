class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climbStairs2(self, n):
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(max(i - 3, 0), i):
                dp[i] += dp[j]

        return dp[-1]
272. Climbing Stairs II
