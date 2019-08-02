class Solution:
    """
    @param A: An integer array
    @param B: An integer array
    @return: Their smallest difference.
    """
    def smallestDifference(self, A, B):
        if len(B) > len(A):
            A, B = B, A

        A.sort()
        B.sort()

        from bisect import bisect_left
        minimum = float("inf")
        for b in B:
            pos = bisect_left(A, b)
            if pos < len(A):
                minimum = min(minimum, abs(b - A[pos]))
            if pos > 0:
                minimum = min(minimum, abs(b - A[pos - 1]))

        return minimum