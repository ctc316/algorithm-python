"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# Version 1: Prefix sum
class Solution:
    """
    @param A: An integer list
    @param queries: An query list
    @return: The result list
    """
    def intervalSum(self, A, queries):
        n = len(A)
        presum = [0 for i in range(n + 1)]
        sum = 0
        for i in range(n):
            sum += A[i]
            presum[i + 1] = sum

        results = []
        for q in queries:
            results.append(presum[q.end + 1] - presum[q.start])

        return results


# Version 2: Binary Index Tree
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
    @param A: An integer list
    @param queries: An query list
    @return: The result list
    """
    def intervalSum(self, A, queries):
        bitree = BITree(A)
        results = []
        for q in queries:
            results.append(bitree.sumRange(q.start, q.end))

        return results
