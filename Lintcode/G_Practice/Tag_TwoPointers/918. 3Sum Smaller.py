class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """
    def threeSumSmaller(self, nums, target):
        n = len(nums)
        res = 0
        sortedNums = sorted([(nums[i], i) for i in range(n)])
        for i in range(n - 2):
            t = target - sortedNums[i][0]
            j = i + 1
            k = n - 1
            while j < k:
                remains = t - sortedNums[j][0] - sortedNums[k][0]
                if remains > 0:
                    res += k - j
                    j += 1
                else:
                    k -= 1

        return res
