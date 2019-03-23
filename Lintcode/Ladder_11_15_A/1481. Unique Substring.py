class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: all unique substring
    """
    def uniqueSubstring(self, s, k):
        records = set()
        for i in range(len(s) - k + 1):
            word = s[i: i + k]
            records.add(word)

        return sorted(records)