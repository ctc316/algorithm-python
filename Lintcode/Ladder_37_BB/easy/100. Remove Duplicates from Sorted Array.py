class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        n = len(nums)
        if n < 2:
            return n

        i = 0
        j = 1

        while j < n:
            while j < n and nums[j] == nums[i]:
                j += 1

            if j >= n:
                break

            i += 1
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

        return i + 1