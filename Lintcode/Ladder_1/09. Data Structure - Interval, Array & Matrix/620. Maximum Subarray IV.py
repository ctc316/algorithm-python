class Solution:
    """
    @param nums: an array of integer
    @param k: an integer
    @return: the largest sum
    """
    def maxSubarray4(self, nums, k):
        n = len(nums)
        if n < k:
            return 0

        prefixSum = [0 for _ in range(n + 1)]
        minIdx = 0
        largest = -sys.maxsize - 1

        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        for i in range(k, n + 1):
            # update minIdx
            if prefixSum[i - k] < prefixSum[minIdx]:
                minIdx = i - k

            # compare
            largest = max(largest, prefixSum[i] - prefixSum[minIdx])

        return largest