class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        n = len(s)
        if n == 0:
            return 0

        dp = [0 for _ in range(n + 1)]
        dp[0] = 1

        for i in range(1, n + 1):
            if int(s[i - 1:i]) > 0:
                dp[i] += dp[i - 1]

            if i - 2 >= 0:
                two_digits = int(s[i - 2:i])
                if two_digits >= 10 and two_digits <= 26:
                    dp[i] += dp[i - 2]

        return dp[-1]