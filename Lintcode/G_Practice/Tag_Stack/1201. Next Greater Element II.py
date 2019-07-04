'''
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

The length of given array won't exceed 10000.

Example
Example 1:

Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: [1]
Output: [-1]
Explanation:
The number 1 can't find next greater number.
'''


'''
[1, 2, 1, 1, 0  3, 1]
[2, 3, 3, 3, 3 -1, 2]


max stack , reverse

'''

class Solution:
    """
    @param nums: an array
    @return: the Next Greater Number for every element
    """
    def nextGreaterElements(self, nums):
        '''
        [1,2,1,1,3,2,3] iterate -> [1,2,1,1,3,2,3,1,2,1,1,3,2]
        init reversed mono stack for idx, 2n - 1 ~ n
        start from n - 1 to 0
        '''
        if not nums or len(nums) == 0:
            return []

        n = len(nums)
        idx_mono_stack = []
        res = [-1 for _ in range(n)]

        # init
        for i in range(n - 2, -1, -1):
            while len(idx_mono_stack) > 0 and nums[i] >= nums[idx_mono_stack[-1]]:
                idx_mono_stack.pop()
            idx_mono_stack.append(i)

        # run results reversely
        for i in range(n - 1, -1, -1):
            while len(idx_mono_stack) > 0 and nums[i] >= nums[idx_mono_stack[-1]]:
                idx_mono_stack.pop()
            if len(idx_mono_stack) > 0:
                res[i] = nums[idx_mono_stack[-1]]
            idx_mono_stack.append(i)

        return res




class Solution:
    """
    @param nums: an array
    @return: the Next Greater Number for every element
    """
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1 for _ in range(n)]
        for i in range(n):
            for j in range(1, n):
                idx = (i + j) % n
                if nums[idx] > nums[i]:
                    res[i] = nums[idx]
                    break

        return res

