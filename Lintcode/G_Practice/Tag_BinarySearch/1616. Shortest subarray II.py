class Solution:
    """
    @param nums:
    @param k:
    @return: return the length of subarray
    """
    def smallestLengthII(self, nums, k):
        n = len(nums)
        prefixSum = [0 for _ in range(n + 1)]
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        start = 1
        end = len(nums)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.isWorkable(prefixSum, k, mid):
                end = mid
            else:
                start = mid + 1

        if self.isWorkable(prefixSum, k, start):
            return start
        elif self.isWorkable(prefixSum, k, end):
            return end
        return -1


    def isWorkable(self, prefixSum, k, length):
        for i in range(len(prefixSum) - length):
            if prefixSum[i + length] - prefixSum[i] >= k:
                return True
        return False