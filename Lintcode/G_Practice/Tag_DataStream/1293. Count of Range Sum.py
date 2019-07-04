class Solution:
    """
    @param nums: a list of integers
    @param lower: a integer
    @param upper: a integer
    @return: return a integer
    """
    def countRangeSum(self, nums, lower, upper):
        prefixSumCnt = {0: 1}
        presum = 0
        result = 0
        for num in nums:
            presum += num
            for j in range(lower, upper + 1):
                if presum - j in prefixSumCnt:
                    result += prefixSumCnt[presum - j]
            prefixSumCnt[presum] = prefixSumCnt.get(presum, 0) + 1

        return result
