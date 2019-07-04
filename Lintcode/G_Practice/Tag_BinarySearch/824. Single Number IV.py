class Solution:
    """
    @param nums: The number array
    @return: Return the single number
    """
    def getSingleNumber(self, nums):
        for i in range(1, len(nums), 2):
            if nums[i] != nums [i - 1]:
                return nums[i - 1]

        return nums[-1]