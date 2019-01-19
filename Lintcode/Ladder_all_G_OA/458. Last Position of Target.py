class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        n = len(nums)
        if n == 0:
            return -1

        left = 0
        right = n - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if target < nums[mid]:
                right = mid
            else:
                left = mid

        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1