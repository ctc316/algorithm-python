class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        n = len(s)
        if n == 0:
            return ""

        longest = 1
        longest_range = (0, 1)

        isPalindrome = [[False for _ in range(n)] for __ in range(n)]
        for i in range(n):
            isPalindrome[i][i] = True

        for i in range(n - 1):
            isPalindrome[i][i + 1] = s[i] == s[i + 1]
            if longest < 2 and isPalindrome[i][i + 1]:
                longest = 2
                longest_range = (i, i + 2)

        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                isPalindrome[i][j] = isPalindrome[i + 1][j - 1] and s[i] == s[j]
                if isPalindrome[i][j] and j - i + 1 > longest:
                    longest = j - i + 1
                    longest_range = [i, j + 1]

        return s[longest_range[0]:longest_range[1]]