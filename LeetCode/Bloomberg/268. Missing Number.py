class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            while nums[i] != i and nums[i] < n:
                t = nums[i]
                nums[i] = nums[t]
                nums[t] = t
            i += 1

        for i in range(n):
            if nums[i] != i: return i

        return n