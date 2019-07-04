class Solution:
    """
    @param citations: a list of integers
    @return: return a integer
    """
    def hIndex(self, citations):
        citations.sort()
        from bisect import bisect_left

        n = len(citations)
        for i in range(1, n + 1):
            idx = bisect_left(citations, i)
            if n - idx < i:
                return i - 1

        return n