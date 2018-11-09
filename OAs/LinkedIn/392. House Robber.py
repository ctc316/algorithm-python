class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        n = len(A)
        dp = [0 for i in range(3)]
        for i in range(n):
            dp[i % 3] = max(dp[(i - 1) % 3], dp[(i - 2) % 3] + A[i])
        
        return dp[(n - 1) % 3]