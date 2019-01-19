class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        if n < 3:
            return False

        left = 0
        right = n - 1
        while left < right and A[left] < A[left + 1]:
            left += 1
        while left < right and A[right - 1] > A[right]:
            right -= 1

        return left == right and left != 0 and left != n - 1