class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        n = len(nums)
        j = 0
        summ = 0
        minimum = n + 1
        for i in range(n):
            while j < n and summ < s:
                summ += nums[j]
                j += 1

            if summ < s:
                break
             
            minimum = min(minimum, j - i)

            summ -= nums[i]


        if minimum > n:
            return -1

        return minimum