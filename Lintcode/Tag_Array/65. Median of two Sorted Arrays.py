class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        k = int(n / 2) + 1
        if n % 2 == 1:
             return self.findK(A, B, 0, 0, k)
        return (self.findK(A, B, 0, 0, k) + self.findK(A, B, 0, 0, k - 1)) / 2


    def findK(self, A, B, a_idx, b_idx, k):
        if a_idx == len(A):
            return B[b_idx + k - 1]

        if b_idx == len(B):
            return A[a_idx + k - 1]

        if k == 1:
            return min(A[a_idx], B[b_idx])

        mid = int(k / 2)

        end_a = min(len(A) - 1, a_idx + mid - 1)
        end_b = min(len(B) - 1, b_idx + mid - 1)
        if A[end_a] < B[end_b]:
            return self.findK(A, B, end_a + 1, b_idx, k - (end_a - a_idx + 1))
        else:
            return self.findK(A, B, a_idx, end_b + 1, k - (end_b - b_idx + 1))