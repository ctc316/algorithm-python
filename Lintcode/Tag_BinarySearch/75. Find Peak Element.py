class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        n = len(A)
        left = 0
        right = n - 1
        while left < right:
            mid = left + (right - left) // 2
            if mid > 0 and A[mid] <= A[mid - 1]:
                right = mid - 1
            elif mid + 1 < n and A[mid] <= A[mid + 1]:
                left = mid + 1
            else:
                return mid

        return left