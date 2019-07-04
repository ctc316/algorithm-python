class Solution:
    """
    @param nums: 4 cards
    @return: whether they could get the value of 24
    """
    def compute24(self, nums):
        return self.dfs(nums, {})

    def dfs(self, nums, memo):
        if len(nums) == 1:
            return abs(nums[-1] - 24) < 10e-7

        if tuple(nums) in memo:
            return memo[tuple(nums)]

        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                a = nums[i]
                b = nums[j]
                comba = self.getCombination(a, b)
                remain = nums[:i] + nums[i + 1 : j] + nums[j + 1 :]
                for c in comba:
                    if self.dfs(remain + [c], memo):
                        memo[tuple(nums)] = True
                        return True

        memo[tuple(nums)] = False
        return False

    def getCombination(self, a, b):
        res = [a + b, a - b, b - a, a * b]
        if a != 0:
            res.append(b / a)
        if b != 0:
            res.append(a / b)
        return res