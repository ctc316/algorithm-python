class Solution:
    """
    @param nums: An array of integers
    @return: nothing
    """
    def nextPermutation(self, nums):
        n = len(nums)
        if n < 2:
            return nums

        '''
            5 1 4 3 2 2 1
              p1      p2

            5 2 4 3 2 1 1
        '''
        # find the first decending point from the left
        p1 = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                p1 = i
                break

        # if the array is sorted in descending order, reverse and return it
        if p1 < 0:
            nums.reverse()
            return nums

        # find the num to swap
        p2 = n - 1
        while nums[p2] <= nums[p1]:
            p2 -= 1

        # swap
        self.swap(nums, p1, p2)

        # reverse left side of p1
        left = p1 + 1
        right = n - 1
        while left < right:
            self.swap(nums, left, right)
            left += 1
            right -= 1


    def swap(self, nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp