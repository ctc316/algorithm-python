# Version 1: hash, Time: O(n * k + mlogm for sorting)
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
            if word in records:
                continue

            records.add(word)

        return sorted(list(records))


# Version 2: Short
class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: all unique substring
    """
    def uniqueSubstring(self, s, k):
        return sorted(list(set(s[i:i + k] for i in range(len(s) - k + 1))))