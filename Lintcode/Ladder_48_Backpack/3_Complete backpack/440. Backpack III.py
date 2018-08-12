# Version 1:  TLE
class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """
    def backPackIII(self, A, V, m):
        dp = [0 for _ in range(m + 1)]
        for i in range(len(A)):
            for j in range(1, int(m / A[i]) + 1):
                for k in range(m, A[i] - 1, -1):
                    dp[k] = max(dp[k], dp[k - A[i]] + V[i])

        return dp[m]



# Version 2: Time Complexity Optimization
# 由於同一種物品的個數無限，所以我們可以在任意容量 j 的背包嘗試裝入當前物品，j 從小向大枚舉可以保證所有包含第 i 種物品，體積不超過 j - A[i] 的狀態被枚舉到。

class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """

    '''
        size: [2,3,5,7]
        value:[1,5,2,4]
        10

            0          5             10
            [0,0,0,0,0,0, 0, 0, 0, 0, 0]
        2,1 [0,0,1,1,1,1, 1, 1, 1, 1, 1]
        3,5 [0,0,1,5,5,6,10,10,11,15,15]
        5,2 [0,0,1,5,5,6,10,10,11,15,15]
        7,4 [0,0,1,5,5,6,10,10,11,15,15]
    '''

    def backPackIII(self, A, V, m):
        dp = [0 for _ in range(m + 1)]
        for i in range(len(A)):
            for j in range(A[i], m + 1):
                dp[j] = max(dp[j], dp[j - A[i]] + V[i])

        return dp[m]

