class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):

        '''
            [5,4,4,3,2,1], 1~5
            3, count = 3,  3~5
            4, count = 5,  3~4
        '''

        left = 1
        right = len(nums) - 1
        while left + 1< right:
            mid = left + int((right - left) / 2)
            if self.count(nums, mid) <= mid:
                left = mid
            else:
                right = mid

        if self.count(nums, left) <= left:
            return right

        return left


    def count(self, nums, mid):
        cnt = 0
        for i in nums:
            if i <= mid:
                cnt += 1

        return cnt
