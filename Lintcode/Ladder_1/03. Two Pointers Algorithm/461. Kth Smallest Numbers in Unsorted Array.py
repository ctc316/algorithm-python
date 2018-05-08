# Version 1: Sorting, Time: O(nlogn)
class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        if len(nums) < k:
            return None

        nums.sort()

        return nums[k - 1]