class Solution:
    """
    @param nums: an integer array
    @return: all the different possible increasing subsequences of the given array
    """
    def findSubsequences(self, nums):
        if not nums:
            return []
            
        results = []
        n = len(nums)
        self.dfs(nums, n, 0, -float("Inf"), [], results)
        return results
        
        
    def dfs(self, nums, n, start, current, combination, results):
        if len(combination) > 1:
            results.append([c for c in combination])
            
        if start == n:
            return
        
        pre_acc = set()
        for i in range(start, n):
            if nums[i] < current:
                continue
            if nums[i] in pre_acc:
                continue
            
            pre_acc.add(nums[i])
            combination.append(nums[i])
            self.dfs(nums, n, i + 1, nums[i], combination, results)
            combination.pop()
