class Solution:
    """
    @param nums: the given array
    @param s: the given target
    @return: the number of ways to assign symbols to make sum of integers equal to target S
    """
    def findTargetSumWays(self, nums, s):
        val_cnts = self.dfs(nums, s, 0)
        if s not in val_cnts:
            return 0
        return val_cnts[s]


    def dfs(self, nums, s, i):
        if i >= len(nums):
            return {0: 1}

        vc = {}
        sub_vc = self.dfs(nums, s, i + 1)
        for k, v in sub_vc.items():
            positive = k + nums[i]
            vc[positive] = vc[positive] + v if positive in vc else v
            negative = k - nums[i]
            vc[negative] = vc[negative] + v if negative in vc else v

        return vc