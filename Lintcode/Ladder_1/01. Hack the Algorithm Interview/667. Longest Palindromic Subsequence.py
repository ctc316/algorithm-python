
# Version 1: DP, Time: O(n^2), Space: (n^2)
class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        if len(s) < 2:
            return len(s)

        """
        https://www.youtube.com/watch?v=_nCsPn7_OgI

            aabdba
            0 1 2 3 4 5
          0 1 2 2
          1   1 1 1
          2     1 1 3
          3       1 1
          4         1 1
          5           1
        """

        length = len(s)

        dp = [[0 for _ in range(length)] for __ in range(length)]

        for i in range(length):
            dp[i][i] = 1

        for i in range(0, length - 1):
            dp[i][i + 1] = 2 if s[i] == s[i + 1] else 1

        for n in range(3, len(s) + 1):
            for i in range(0, len(s) - n + 1):
                j = i + n - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][length - 1]