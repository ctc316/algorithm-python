class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """
    def previousPermuation(self, nums):
        '''
            1 2 3 4 5 3 2 1
                       p1 p2
            1 2 3 4 5 3 1 2
                      p1  p2
            1 2 3 4 5 2 3 1
                       p1 p2
            1 2 3 4 5 2 1 3

        '''
        n = len(nums)

        # find the first decsending index p1 from the left
        p1 = n - 2
        while p1 > -1 and nums[p1] <= nums[p1 + 1]:
            p1 -= 1

        if p1 < 0:
            nums.reverse()
            return nums


        # find the first num < p1 from the left
        p2 = n - 1
        while p2 > p1 and nums[p2] >= nums[p1]:
            p2 -= 1


        # swap p1, p2
        self.swap(nums, p1, p2)


        # reverse all the right side numbers of p1
        left = p1 + 1
        right = n - 1
        while left < right:
            self.swap(nums, left, right)
            left += 1
            right -= 1

        return nums


    def swap(self, nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp