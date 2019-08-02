class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        '''
            "" l i n t c o d e
        ""  T
        l      F F F T F F F F
        i        F F T F
        n            T
        t            T
        c                    T
        o                F
        d                  F
        e                    F

        [i][j] <- [i - 1][i - 1] == True and s[i:j+1] in dict
        '''

        n = len(s)
        min_len = n
        max_len = 0
        for d in dict:
            min_len = min(min_len, len(d))
            max_len = max(max_len, len(d))

        dp = [False] * (n + 1)
        dp[0] = True
        for i, ch in enumerate(s):
            if not dp[i]:
                continue
            for j in range(i + min_len - 1, min(i + max_len, n)):
                if s[i : j + 1] in dict:
                    dp[j + 1] = True

            if dp[-1]:
                break

        return dp[-1]