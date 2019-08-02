class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        idx, i, j = m + n - 1, m - 1, n - 1
        while i > -1 and j > -1:
            if A[i] > B[j]:
                A[idx] = A[i]
                i -= 1
            else:
                A[idx] = B[j]
                j -= 1
            idx -= 1

        while i > -1:
            A[idx] = A[i]
            i -= 1
            idx -= 1

        while j > -1:
            A[idx] = B[j]
            j -= 1
            idx -= 1