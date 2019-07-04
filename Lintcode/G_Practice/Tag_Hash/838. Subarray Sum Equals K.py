class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsK(self, nums, k):
        psum_cnts = {0: 1}
        summ = 0
        res = 0
        for num in nums:
            summ += num
            if summ - k in psum_cnts:
                res += psum_cnts[summ - k]

            psum_cnts[summ] = psum_cnts[summ] + 1 if summ in psum_cnts else 1

        return res