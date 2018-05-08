# Version 1: Enumeration from center, Time: O(n^2)
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ""

        longest = 0
        start = 0
        for i in range(len(s)):
            # Odd
            count = self.explorePalindrome(s, i, i)
            if count > longest:
                longest = count
                start = i - int(count / 2)

            # Even
            if i + 1 == len(s):
                break

            count = self.explorePalindrome(s, i, i + 1)
            if count > longest:
                longest = count
                start = i - int(count / 2) + 1

        return s[start : start + longest]


    def explorePalindrome(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            count = right - left + 1
            left -= 1
            right += 1

        return count



# Version 2: DP, Time: O(n^2), Space: O(n^2)
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ""

        sLen = len(s)
        start = 0
        longest = 1

        # build a matrix that indicates whether i to j is palindrom
        isPalindrome = [[False for i in range(sLen)] for j in range(sLen)]

        # i = i
        for i in range(sLen):
            isPalindrome[i][i] = True

        # check if i == i + 1
        for i in range(0, sLen - 1):
            if s[i] == s[i + 1]:
                isPalindrome[i][i + 1] = True
                start = i
                longest = 2


        # "aabcdzdcab"
        #         i j
        #        i  j
        # reverse iteration because we determined the palindrome matrix by i to j
        # therefore, we have to start from the smaller range
        for i in range(sLen - 3, -1, -1):
            for j in range(i + 2, sLen):
                if isPalindrome[i + 1][j - 1] and s[i] == s[j]:
                    isPalindrome[i][j] = True
                    count = j - i + 1
                    if count > longest:
                        longest = count
                        start = i

        return s[start : start + longest]