class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)
        start = 0
        results = []
        for i in range(1, len(nums) + 1):
            if i == n or nums[i] != nums[i - 1] + 1:
                if start == i - 1:
                    results.append(str(nums[i - 1]))
                else:
                    results.append(str(nums[start]) + "->" + str(nums[i - 1]))
                start = i

        return results