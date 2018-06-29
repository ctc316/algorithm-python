class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        preMin = preMax = nums[0]
        minProd = maxProd = nums[0]
        largest = nums[0]
        for i in range(1, n):
            maxProd = max(nums[i], preMin * nums[i], preMax * nums[i])
            minProd = min(nums[i], preMin * nums[i], preMax * nums[i])
            largest = max(largest, maxProd)
            preMax = maxProd
            preMin = minProd

        return largest