class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        n = len(nums)
        presum = [0 for _ in range(n + 1)]
        summ = 0
        for i in range(n):
            summ += nums[i]
            presum[i + 1] = summ
            
        records = {}
        records[0] = 0  #presum: idx
        longest = 0
        for i in range(1, n + 1):
            target = presum[i] - k
            if target in records:
                longest = max(longest, i - records[target])
            
            if presum[i] not in records:
                records[presum[i]] = i
                
        return longest