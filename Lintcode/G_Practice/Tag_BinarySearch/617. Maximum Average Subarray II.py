class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        '''
        找一段长度 >= k 的子数组使它的平均值满足条件。
        Sum 是 0 到 i 所有元素之和，而 prevSum 是 0 到 i - k 的所有元素之和，
        这样可以保证用 Sum - PreSum 的数组长度比 k 长
        prevMin 来记录 prevSum 的最小值，通过 sum 减去 prevMin 来获得子数组可能的最大值

        '''
        self.n = len(nums)
        nums = [float(x) for x in nums]
        start = min(nums)
        end = max(nums)
        while start + 1e-6 < end:
            mid = start + (end - start) / 2
            if self.has_greater_avg(nums, k, mid):
                start = mid
            else:
                end = mid
        return start


    def has_greater_avg(self, nums, k, mid):
        summ = 0.0
        prev_sum = 0.0
        prev_min = 0.0
        for i in range(self.n):
            summ += nums[i] - mid
            if i >= k - 1 and summ >= 0:
                return True

            if i >= k:
                prev_sum += nums[i - k] - mid
                prev_min = min(prev_min, prev_sum)
                if summ - prev_min >= 0:
                    return True

        return False
