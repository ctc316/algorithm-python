# Version 1: Brute Froce, Time: O(n)
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        if nums is None or len(nums) == 0:
            return None

        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                return nums[i + 1]

        return nums[0]



# Version 2: Binary Search, Time: O(n)
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        if nums is None or len(nums) == 0:
            return None

        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if nums[mid] == nums[end]:
                # [1, 1, 1, 1, 0, 1, 1], 0 might hide in the area
                #          mid      end
                end -= 1
            elif nums[mid] > nums[end]:
                # search the right side
                start = mid
            else:
                end = mid


        return min(nums[start], nums[end])