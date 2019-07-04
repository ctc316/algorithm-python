class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        '''
            "" a a a b c
        ""  T  F F F F F
        a   F  T F F F F
        *   F  F T T F F
        ?   F  F F T T F
        c   F  F F F F T

        if [prev][j - 1] == T and ch_p == * or ? or ch_s  --> T
        if ([prev][j] or [cur][j - 1]) and ch_p == *      --> T
        '''

        n = len(p)
        m = len(s)

        dp = [[False for _ in range(m + 1)] for __ in range(2)]
        dp[0][0] = True

        for i in range(1, n + 1):
            prev = (i - 1) % 2
            cur = i % 2

            dp[cur][0] = dp[prev][0] and p[i - 1] == '*'

            for j in range(1, m + 1):
                if  dp[prev][j - 1] and (p[i - 1] == s[j - 1] or p[i - 1] == '?' or p[i - 1] == '*')  \
                    or (dp[prev][j] or dp[cur][j - 1]) and p[i - 1] == '*':
                        dp[cur][j] = True
                else:
                    dp[cur][j] = False

        return dp[n % 2][m]