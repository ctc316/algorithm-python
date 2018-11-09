class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        n = len(A)
        if n < 2:
            return n

        longest = 0
        
        conti = 1
        for i in range(1, n):
            if A[i] > A[i - 1]:
                conti += 1
            else:
                conti = 1
            longest = max(longest, conti)

        conti = 1
        for i in range(1, n):
            if A[i] < A[i - 1]:
                conti += 1
            else:
                conti = 1
            longest = max(longest, conti)

        return longest