class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1

        for size in nums:
            for i in range(target, size - 1, -1):
                dp[i] += dp[i - size]

        return dp[target]