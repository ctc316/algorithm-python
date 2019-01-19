class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def productExceptSelf(self, nums):
        n = len(nums)
        output = [1 for _ in range(n)]

        multiply = 1
        for i in range(n):
            output[i] *= multiply
            multiply *= nums[i]

        multiply = 1
        for i in range(n - 1, -1, -1):
            output[i] *= multiply
            multiply *= nums[i]

        return output