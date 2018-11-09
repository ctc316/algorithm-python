class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        n = len(s)
        if n == 0 or k == 0:
            return 0

        counts = {}
        longest = 0
        j = 0
        for i in range(n):
            while j < n and (s[j] in counts or len(counts) < k):
                if s[j] in counts:
                    counts[s[j]] += 1
                else:
                    counts[s[j]] = 1

                j += 1

            longest = max(longest, j - i)

            counts[s[i]] -= 1
            if counts[s[i]] == 0:
                del counts[s[i]]

        return longest