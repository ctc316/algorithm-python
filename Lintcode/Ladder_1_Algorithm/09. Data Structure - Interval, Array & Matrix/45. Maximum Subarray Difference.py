class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """
    def maxDiffSubArrays(self, nums):
        n = len(nums)
        if n < 2:
            return 0

        # fill out the maximum and minimum sum from the left
        l_mins = [0 for _ in range(n)]
        l_maxs = [0 for _ in range(n)]
        l_mins[0] = l_maxs[0] = summ = nums[0]
        maxi = mini = 0
        for i in range(1, n):
            mini = min(mini, summ)
            maxi = max(maxi, summ)
            summ += nums[i]
            l_maxs[i] = max(l_maxs[i - 1], summ - mini)
            l_mins[i] = min(l_mins[i - 1], summ - maxi)


        # fill out the maximum and minimum sum from the right
        r_mins = [0 for _ in range(n)]
        r_maxs = [0 for _ in range(n)]
        r_mins[n - 1] = r_maxs[n - 1] = summ = nums[n - 1]
        maxi = mini = 0
        for i in range(n - 2, -1, -1):
            mini = min(mini, summ)
            maxi = max(maxi, summ)
            summ += nums[i]
            r_maxs[i] = max(r_maxs[i + 1], summ - mini)
            r_mins[i] = min(r_mins[i + 1], summ - maxi)


        # find the largest difference pairs
        largest = -sys.maxsize - 1
        for i in range(1, n):
            largest = max(largest, l_maxs[i - 1] - r_mins[i], r_maxs[i] - l_mins[i - 1])


        return largest