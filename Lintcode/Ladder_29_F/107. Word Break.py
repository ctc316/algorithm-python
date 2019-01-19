class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        n = len(s)
        if n == 0:
            return True

        dict = list(dict)
        dict.sort(key=lambda x: len(x))

        dp = [False for i in range(n + 1)]
        dp[0] = True

        for i in range(1, n + 1):
            for d in dict:
                j = i - len(d)
                if j < 0:
                    break

                if dp[j] and s[j:i] == d:
                   dp[i] = True

        return dp[-1]