class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        counts = {}
        for ch in s:
            if ch not in counts:
                counts[ch] = 1
            else:
                counts[ch] += 1

        odd = False
        length = 0
        for cnt in counts.values():
            if cnt % 2 == 1:
                odd = True
                length += cnt - 1
            else:
                length += cnt

        if odd:
            length += 1

        return length