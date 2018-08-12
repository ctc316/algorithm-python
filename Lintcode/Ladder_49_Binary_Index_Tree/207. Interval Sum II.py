class BITree:
    def __init__(self, nums):
        self.n = len(nums)
        self.arr = [0 for _ in range(self.n)]
        self.bitree = [0 for _ in range(self.n + 1)]

        for i in range(self.n):
            self.update(i, nums[i])

    def update(self, i, val):
        diff = val - self.arr[i]
        self.arr[i] = val

        i += 1
        while i <= self.n:
            self.bitree[i] += diff
            i += i & (-i)


    def sumRange(self, i, j):
        return self._getSum(j) - self._getSum(i - 1)


    def _getSum(self, i):
        i += 1
        sum = 0
        while i > 0:
            sum += self.bitree[i]
            i -= i & (-i)

        return sum


class Solution:
    """
    @param: A: An integer array
    """
    def __init__(self, A):
        self.bitree = BITree(A)

    """
    @param: start: An integer
    @param: end: An integer
    @return: The sum from start to end
    """
    def query(self, start, end):
        return self.bitree.sumRange(start, end)

    """
    @param: index: An integer
    @param: value: An integer
    @return: nothing
    """
    def modify(self, index, value):
        self.bitree.update(index, value)