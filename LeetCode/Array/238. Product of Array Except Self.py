# Version 1: build products of before and after i, Time: O(n), Space: O(n)
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # scan from left to right to find products before i
        before_i = [i for i in range(len(nums))]
        prod = 1
        for i in range(len(nums)):
            before_i[i] = prod
            prod *= nums[i]

        # scan from left to right to find products after i
        after_i = [i for i in range(len(nums))]
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            after_i[i] = prod
            prod *= nums[i]

        return [before_i[i] * after_i[i] for i in range(len(nums))]



# Version 2: save extra space, Time: O(n), Space: O(1)
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        products = [i for i in range(len(nums))]

        # scan from left to right to find products before i
        prod = 1
        for i in range(len(nums)):
            products[i] = prod
            prod *= nums[i]

        # scan from left to right to mutiply products after i
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= prod
            prod *= nums[i]

        return products