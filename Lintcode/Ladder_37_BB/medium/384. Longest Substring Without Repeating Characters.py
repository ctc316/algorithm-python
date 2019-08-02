class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        longest = 0
        chars = set()
        j = 0
        for i in range(n):
            while j < n and s[j] not in chars:
                chars.add(s[j])
                j += 1
            if j - i > longest:
                longest = j - i
            chars.remove(s[i])

        return longest