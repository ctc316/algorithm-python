# Version 1: space: O(N * M)
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        n = len(A)
        dp = [[0 for _ in range(m + 1)] for __ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] <= j:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i - 1]] + V[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][m]




# Version 2: Space: O(m)
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        '''
            10
            [4,2,3,5,6]
            [1,2,4,6,0]

                0          5           10
            dp  [0,0,0,0,0,0,0,0, 0, 0, 0]
            4,1 [0,0,0,0,1,1,1,1, 1, 1, 1]
            2,2 [0,0,2,2,2,2,3,3, 3, 3, 3]
            3,4 [0,0,2,4,4,6,6,6, 6, 7, 7]
            5,6 [0,0,2,4,4,6,6,8,10,10,12]
            6,0 [0,0,2,4,4,6,6,8,10,10,12]
        '''

        n = len(A)
        dp = [0 for _ in range(m + 1)]
        for i in range(n):
            for j in range(m, A[i] - 1 , -1):
                dp[j] = max(dp[j], dp[j - A[i]] + V[i])

        return dp[m]