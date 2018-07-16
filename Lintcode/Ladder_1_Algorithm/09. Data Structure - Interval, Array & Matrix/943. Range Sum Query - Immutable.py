class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        '''
           [-2, 0, 3, -5, 2, -1]
        [0, -2,-2, 1, -4,-2, -3]

        '''
        self.prefixSum = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            self.prefixSum[i + 1] = self.prefixSum[i] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefixSum[j + 1] - self.prefixSum[i]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)