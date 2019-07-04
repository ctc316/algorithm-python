class Solution:
    """
    @param nums: a list of integers
    @param m: an integer
    @return: return a integer
    """
    def splitArray(self, nums, m):
        l = max(nums)
        r = sum(nums)
        while l + 1 < r:
            mid = l + (r - l) // 2
            if self.canSplitTo(nums, mid) <= m:
                r = mid
            else:
                l = mid

        if self.canSplitTo(nums, l) <= m:
            return l
        return r


    def canSplitTo(self, nums, target):
        subarrays = 1
        summ = 0
        for num in nums:
            summ += num
            if summ > target:
                subarrays += 1
                summ = num
        return subarrays