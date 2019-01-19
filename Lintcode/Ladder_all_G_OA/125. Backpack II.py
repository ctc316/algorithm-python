class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        dp = [0 for _ in range(m + 1)]
        size, val = 0, 0
        for i in range(len(A)):
            size = A[i]
            val = V[i]
            for j in range(m, size - 1, -1):
                dp[j] = max(dp[j], dp[j - size] + val)

        return dp[m]