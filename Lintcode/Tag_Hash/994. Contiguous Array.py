class Solution:
    """
    @param nums: a binary array
    @return: the maximum length of a contiguous subarray
    """
    def findMaxLength(self, nums):
        n = len(nums)
        
        zeros = 0
        ones = 0

        rec_extra_zeros = {} # extra_zeros, idx
        rec_extra_zeros[0] = 0

        longest = 0

        for i in range(n):
            if nums[i] == 0:
                zeros += 1
            else:
                ones += 1

            extra_zeros = zeros - ones
            if extra_zeros in rec_extra_zeros:
                longest = max(longest, i + 1 - rec_extra_zeros[extra_zeros])
            else:
                rec_extra_zeros[extra_zeros] = i + 1


        return longest