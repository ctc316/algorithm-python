class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        n = len(A)
        if n == 0:
            return -1

        left = 0
        right = n - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if A[mid] > A[-1]:
                if A[left] <= target and target <= A[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if A[mid] <= target and target <= A[right]:
                    left = mid
                else:
                    right = mid

        if A[left] == target:
            return left
        elif A[right] == target:
            return right

        return -1