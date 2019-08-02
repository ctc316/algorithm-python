class Solution:
    """
    @param s: a string
    @return: it's index
    """
    def firstUniqChar(self, s):
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
        return -1