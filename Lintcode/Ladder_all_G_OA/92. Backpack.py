class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        dp = [0 for _ in range(m + 1)]
        for size in A:
            for i in range(m, size - 1, -1):
                dp[i] = max(dp[i], dp[i - size] + size)

        return dp[m]