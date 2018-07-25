class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        '''
            dp[j]: 體積不超過 j 的情況下所能得到的最大體積

            10  [3,4,8,5]

               0         5         10
              [0,0,0,0,0,0,0,0,0,0,0]
            3 [0,0,0,3,3,3,3,3,3,3,3]
            4 [0,0,0,3,4,4,4,7,7,7,7]
            8 [0,0,0,3,4,4,4,4,8,8,8]
            5 [0,0,0,3,4,5,5,5,8,9,9]
        '''

        dp = [0 for _ in range(m + 1)]
        for item in A:
            for j in range(m, item - 1, -1):
                dp[j] = max(dp[j], dp[j - item] + item)

        return dp[m]