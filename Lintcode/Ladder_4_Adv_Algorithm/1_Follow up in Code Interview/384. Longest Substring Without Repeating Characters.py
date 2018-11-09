class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        records = {}
        longest = 0
        i = 0
        j = 0
        while j < n:
            if s[j] in records and records[s[j]] >= i:
                i = records[s[j]] + 1

            records[s[j]] = j
            j += 1
            longest = max(longest, j - i)

        return longest