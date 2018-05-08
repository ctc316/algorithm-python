# Version 1: build map for counting each alphabets
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        if len(s) == 0:
            return 0

        # builc dict for ch:count
        dict = {}
        for ch in s:
            if ch in dict:
                dict[ch] = dict.get(ch) + 1
            else:
                dict[ch] = 1

        # find longest
        longest = 0
        middle = 0
        for k, v in dict.items():
            while v > 1:
                v -= 2
                longest += 2

            if v == 1 and middle == 0:
                middle = 1


        return longest + middle


# Version 2: use Hash to find odd nums and remove from string
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s

        odd = set()

        for ch in s:
            if ch in odd:
                odd.remove(ch)
            else:
                odd.add(ch)

        if len(odd) > 0:
            return len(s) - len(odd) + 1

        return len(s)
