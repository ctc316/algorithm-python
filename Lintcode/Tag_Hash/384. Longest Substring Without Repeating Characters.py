class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        '''
            abcabcbb
             ^ ^
        '''
        n = len(s)
        records = {}
        longest = 0
        nonrepeat_idx = 0
        for i in range(n):
            if s[i] in records:
                prev = records[s[i]]
                nonrepeat_idx = max(nonrepeat_idx, prev + 1)

            records[s[i]] = i
            longest = max(longest, i - nonrepeat_idx + 1)

        return longest