class Solution:
    """
    @param nums: a list of integers
    @return: return a list of integers
    """
    def countSmaller(self, nums):
        if len(nums) == 0:
            return []

        # do discretization to make it strictly O(nlogn)
        self._discretize(nums)

        minimum = min(nums)
        n = max(nums) - minimum + 1   # +1 since we like the range to be 1 ~ ...
        bitree = [0 for _ in range(n + 1)]
        results = []
        for i in range(len(nums) - 1, -1, -1):
            # normaization, +1 since we like the range to be 1 ~ ..
            normalizedNum = nums[i] - minimum + 1

            # query prefix sum of previous index
            results.append(self._query(bitree, normalizedNum - 1))

            # update
            self._addOne(bitree, normalizedNum)

        results.reverse()
        return results


    def _discretize(self, nums):
        import bisect
        sortedNums = list(sorted(nums))
        for i in range(len(nums)):
            nums[i] = bisect.bisect_left(sortedNums, nums[i]) + 1


    def _query(self, bitree, i):
        sum = 0
        while i > 0:
            sum += bitree[i]
            i -= i & (-i)

        return sum


    def _addOne(self, bitree, i):
        n = len(bitree)
        while i < n:
            bitree[i] += 1
            i += i & (-i)