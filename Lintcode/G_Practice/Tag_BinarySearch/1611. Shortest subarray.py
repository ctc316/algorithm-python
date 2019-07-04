class Solution:
    """
    @param nums: 
    @param k: 
    @return: return the length of shortest subarray
    """
    def smallestLength(self, nums, k):
        n = len(nums)
        j = summ = 0
        res = float("Inf")
        for i in range(n):
            while j < n and summ < k:
                summ += nums[j]
                j += 1
            if summ >= k:
                res = min(res, j - i)
            summ -= nums[i]
        return res if res != float("Inf") else -1