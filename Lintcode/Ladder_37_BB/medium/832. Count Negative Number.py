class Solution:
    """
    @param nums: the sorted matrix
    @return: the number of Negative Number
    """
    def countNumber(self, nums):
        if not nums or not nums[0]:
            return 0

        n = len(nums)
        m = len(nums[0])
        i = 0
        j = m - 1
        count = 0
        while i < n and j > -1:
            if nums[i][j] >= 0:
                j -= 1
            else:
                count += j + 1
                i += 1

        return count