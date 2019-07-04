class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """
    def findMaxConsecutiveOnes(self, nums):
        cur = before0 = maxi = 0
        for num in nums:
            cur += 1
            if num == 0:
                cur -= before0
                before0 = cur
            maxi = max(maxi, cur)

        return maxi