class Solution:
    """
    @param A: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        from bisect import bisect_left
        A.sort()
        return [bisect_left(A, q) for q in queries]
