class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        if nums is None or len(nums) == 0:
            return -1

        left = 0
        right = len(nums) - 1
        mid = 0
        while left < right - 1:
            mid = int(left + (right - left) / 2)
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid
            else:
                return mid

        if nums[left] == target:
            return left

        if nums[right] == target:
            return right

        return -1