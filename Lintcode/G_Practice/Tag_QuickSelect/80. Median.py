class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """
    def median(self, nums):
        n = len(nums)
        if n % 2 == 1:
            return self.findKthLargest(nums, 0, n - 1, n // 2 + 1)
        return self.findKthLargest(nums, 0, n - 1, n // 2 + 1)

    # quick select
    def findKthLargest(self, A, start, end, k):
        pivot = A[(start + end) // 2]
        left, right = start, end
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        '''
        1 2 3 4 5
        s r   l e

        '''
        pos_k = end - k + 1
        if pos_k <= right:
            return self.findKthLargest(A, start, right, k - (end - right))
        if pos_k >= left:
            return self.findKthLargest(A, left, end, k)

        return A[pos_k]