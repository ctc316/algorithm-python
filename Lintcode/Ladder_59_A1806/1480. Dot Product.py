class Solution:
    """
    @param A: an array
    @param B: an array
    @return: dot product of two array
    """
    def dotProduct(self, A, B):
        n = len(A)
        if n == 0 or len(B) != n:
            return -1

        prod = 0
        for i in range(n):
            prod += A[i] * B[i]

        return prod