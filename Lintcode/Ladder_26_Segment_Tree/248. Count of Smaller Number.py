# Version 1: Sorting + Binary Search
class Solution:
    """
    @param A: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        import bisect
        A.sort()
        results = []
        for q in queries:
            results.append(bisect.bisect_left(A, q))

        return results