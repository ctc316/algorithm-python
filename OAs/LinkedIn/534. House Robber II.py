class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber2(self, nums):
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(self.houseRobber(nums[:-1]), self.houseRobber(nums[1:]))


    def houseRobber(self, A):
        n = len(A)
        dp = [0 for i in range(3)]
        for i in range(n):
            dp[i % 3] = max(dp[(i - 1) % 3], dp[(i - 2) % 3] + A[i])

        return dp[(n - 1) % 3]