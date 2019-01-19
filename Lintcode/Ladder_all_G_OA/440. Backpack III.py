class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """
    def backPackIII(self, A, V, m):
        dp = [0 for _ in range(m + 1)]
        size, val = 0, 0
        for i in range(len(A)):
            size, val = A[i], V[i]
            for j in range(size, m + 1):
                dp[j] = max(dp[j], dp[j - size] + val)

        return dp[m]