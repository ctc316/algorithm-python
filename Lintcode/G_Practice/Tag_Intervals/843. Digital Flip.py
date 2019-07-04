'''
Given an array of 01. You can flip 1 to be 0 or flip 0 to be 1.

Find the minimum number of flipping steps so that the array meets the following rules:

The back of 1 can be either1 or 0, but0 must be followed by 0.

The length of the given array n <= 100000.

Example 1:

Input: [1,0,0,1,1,1]
Output: 2
Explanation: Turn two 0s into 1s.
Example 2:

Input: [1,0,1,0,1,0]
Output: 2
Explanation: Turn the second 1 and the third 1 into 0.
'''


class Solution:
    """
    @param nums: the array
    @return: the minimum times to flip digit
    """
    def flipDigit(self, nums):
        l_zeros = 0
        l_ones = 0
        r_zeros = 0
        r_ones = 0
        for num in nums:
            if num == 1:
                r_ones += 1
            elif num == 0:
                r_zeros += 1

        minimum = r_ones
        for num in nums:
            if num == 1:
                r_ones -= 1
                l_ones += 1
            elif num == 0:
                r_zeros -= 1
                l_zeros += 1
            minimum = min(minimum, l_zeros + r_ones)

        return minimum



class Solution:
    """
    @param nums: the array
    @return: the minimum times to flip digit
    """
    def flipDigit(self, nums):
        pre0, pre1 = 0, 0
        for num in nums:
            if num:
                pre0, pre1 = min(pre0, pre1) + 1, pre1
            else:
                pre0, pre1 = min(pre0, pre1), pre1 + 1

        return min(pre0, pre1)