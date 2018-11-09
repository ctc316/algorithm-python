class Solution:
    """
    @param nums: the given array
    @return: the minimum difference between their sums
    """
    def findMin(self, nums):
        total = sum(nums)
        half = int(total / 2) + 1
        dp = [False for _ in range(half + 1)]
        dp[0] = True

        minimum = sys.maxsize
        for i in nums:
            for j in range(half, i - 1, -1):
                dp[j] |= dp[j - i];
                if dp[j]:
                    minimum = min(minimum, abs(total - j * 2))

        return minimum