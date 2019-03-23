class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        if k == 0:
            return []

        summ = 0
        for i in range(k - 1):
            summ += nums[i]

        res = []
        for i in range(k - 1, len(nums)):
            summ += nums[i]
            res.append(summ)
            summ -= nums[i - k + 1]

        return res