class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        if nums == None or k < 1 or len(nums) < k:
            return []

        results = []

        sum = 0
        for i in range(k):
            sum += nums[i]

        results.append(sum)

        for i in range(k, len(nums)):
            sum -= nums[i - k]
            sum += nums[i]
            results.append(sum)

        return results