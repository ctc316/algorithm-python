class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.arr = [0 for _ in range(self.n)]          # 0 ~ n - 1
        self.BITree = [0 for _ in range(self.n + 1)]   # 0 ~ n

        for i in range(self.n):
            self.update(i, nums[i])


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.arr[i]

        # update nums
        self.arr[i] = val

        # update BITree
        i += 1
        while i <= self.n:
            self.BITree[i] += diff
            i += i & (-i)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > j or i < 0 or j >= self.n:
            return 0

        return self._getSum(j) - self._getSum(i - 1)


    def _getSum(self, i):
        """
        :type i: int
        """
        sum = 0
        i += 1
        while i > 0:
            sum += self.BITree[i]
            i -= i & (-i)

        return sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)