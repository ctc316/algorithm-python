class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        n = len(nums)
        if n < 2:
            return nums

        '''
                [1,3,2,3,2,1]
                    p1 p2

            swap: [1,3,3,2,2,1]

            reverse p1+1 ~ n-1: [1,3,3,1,2,2]
        '''

        # find the first acsending pair from the right
        p1 = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                p1 = i
                break

        # if the array is sorted in descending order, reverse and return it
        if p1 < 0:
            nums.reverse()
            return nums

        # find the first element that is greater than nums[i]
        p2 = n - 1
        while p2 > p1 and nums[p2] <= nums[p1]:
            p2 -= 1

        # swap p1, p2
        self.swap(nums, p1, p2)

        # reverse the right side
        self.reverse(nums, p1 + 1, n - 1)

        return nums


    def swap(self, nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp


    def reverse(self, nums, start, end):
        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1
