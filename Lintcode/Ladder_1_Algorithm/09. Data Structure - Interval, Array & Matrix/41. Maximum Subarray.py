class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        n = len(nums)
        prefixSum = [0 for _ in range(n + 1)]
        minIdx = 0
        largeSum = -sys.maxsize - 1
        for i in range(1, n + 1):
            # update prefixSum
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1]

            # compare
            largeSum = max(largeSum, prefixSum[i] - prefixSum[minIdx])

            # update minIdx
            if prefixSum[i] < prefixSum[minIdx]:
                minIdx = i

        return largeSum