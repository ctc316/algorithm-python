class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        
        # fill out the maximum sum array from the left
        l_maxs = [0 for _ in range(n)]
        l_maxs[0] = summ = nums[0]
        mini = 0
        for i in range(1, n):
            mini = min(mini, summ)
            summ += nums[i]
            l_maxs[i] = max(l_maxs[i - 1], summ - mini)
            
        
        # fill out the maximum sum array from the right 
        r_maxs = [0 for _ in range(n)]
        r_maxs[n - 1] = summ = nums[n - 1]
        mini = 0
        for i in range(n - 2, -1, -1):
            mini = min(mini, summ)
            summ += nums[i]
            r_maxs[i] = max(r_maxs[i + 1], summ - mini)
            
        # compare and choose the largest pair
        largest = -sys.maxsize - 1
        for i in range(1, n):
            largest = max(largest, l_maxs[i - 1] + r_maxs[i])

        return largest