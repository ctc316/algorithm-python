class Solution:
    """
    @param s: The string s
    @param t: The string t
    @return: Return if can get the string t
    """
    def canGetString(self, s, t):
        n = len(s)
        m = len(t)
        if n < m:
            return False

        i = 0
        j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                j += 1
            i += 1

        return j == m



class Solution:
    """
    @param s: The string s
    @param t: The string t
    @return: Return if can get the string t
    """
    def canGetString(self, s, t):
        '''
            ""  b  c  a
        ""  T   F  F  F
        a   T   F  F  F
        b   T   T  F  F
        c   T   F  T  F

        [i - 1][j] or [i - 1][j - 1] and ch_s == ch_t
        '''

        n = len(s)
        m = len(t)

        if n < m:
            return False

        dp = [[False for _ in range(m + 1)] for __ in range(2)]
        dp[0][0] = True

        for i in range(1, n + 1):
            cur = i % 2
            prev = (i - 1) % 2
            for j in range(m + 1):
                dp[cur][j] = dp[prev][j] or dp[prev][j - 1] and s[i - 1] == t[j - 1]

        return dp[n % 2][m]