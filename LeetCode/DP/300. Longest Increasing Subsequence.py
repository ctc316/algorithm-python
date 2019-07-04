class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        maxi = 0
        for i in range(0, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
            if dp[i] > maxi:
                maxi = dp[i]
                
        return maxi
                
            


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.dfs(nums, 0, float('-inf'), {})

    def dfs(self, nums, start, cur, records):
        key = "{}_{}".format(start,cur)
        if key in records:
            return records[key]

        longest = 0
        for i in range(start, len(nums)):
            if nums[i] > cur:
                longest = max(longest, self.dfs(nums, i + 1, nums[i], records) + 1)

        records[key] = longest
        return longest