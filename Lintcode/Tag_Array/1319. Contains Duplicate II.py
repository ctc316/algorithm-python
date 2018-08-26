class Solution:
    """
    @param nums: the given array
    @param k: the given number
    @return:  whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k
    """
    def containsNearbyDuplicate(self, nums, k):
        records = {}
        for i in range(len(nums)):
            if nums[i] in records and i - records[nums[i]] <= k:
                    return True

            records[nums[i]] = i

        return False