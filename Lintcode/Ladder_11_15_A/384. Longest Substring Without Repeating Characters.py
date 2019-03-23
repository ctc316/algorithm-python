class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        longest = 0
        chars = set()
        i = 0
        j = 0
        while j < n:
            while j < n and s[j] not in chars:
                chars.add(s[j])
                j += 1

            if j - i > longest:
                longest = j - i

            chars.remove(s[i])
            i += 1

        return longest