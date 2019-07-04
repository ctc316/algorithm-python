class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def wiggleSort(self, nums):
        self.quickSort(nums, 0, len(nums) - 1)
        for i in range(2, len(nums), 2):
            nums[i], nums[i - 1] = nums[i - 1], nums[i]


    def quickSort(self, nums, start, end):
        if start >= end:
            return

        pivot = nums[start + (end - start) // 2]
        left = start
        right = end
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        self.quickSort(nums, start, right)
        self.quickSort(nums, left, end)
