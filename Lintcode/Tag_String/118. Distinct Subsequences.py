class Solution:
    """
    @param: : A string
    @param: : A string
    @return: Count the number of distinct subsequences
    """

    def numDistinct(self, S, T):
        '''
           n
        m    r a b b b i t
           1 1 1 1 1 1 1 1
        r  0 1 1 1 1 1 1 1
        a  0 0 1 1 1 1 1 1
        b  0 0 0 1 2 3 3 3
        b
        i
        t
        '''
        n = len(S)
        m = len(T)
        dp = [[0 for _ in range(n + 1)] for __ in range(m + 1)]
        for j in range(n + 1):
            dp[0][j] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1]
                if T[i - 1] == S[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]


        return dp[-1][-1]