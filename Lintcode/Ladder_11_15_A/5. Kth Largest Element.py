class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        if len(nums) < n:
            return -1

        return self.__quickSelect(nums, 0, len(nums) - 1, n)


    def __quickSelect(self, nums, start, end, k):
        pivot = nums[(start + end) // 2]
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1

            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # 0, 1, 2, 3, 4, 5    k=2, pos=5-2+1
        pos = end - k + 1
        if pos >= left:
            return self.__quickSelect(nums, left, end, k)
        elif pos <= right:
            return self.__quickSelect(nums, start, right, k - (end - right))
        return nums[right + 1]