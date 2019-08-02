class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        min_pref = 0
        max_sum = float("-inf")
        summ = 0
        for num in nums:
            summ += num
            max_sum = max(max_sum, summ - min_pref)
            min_pref = min(min_pref, summ)

        return max_sum