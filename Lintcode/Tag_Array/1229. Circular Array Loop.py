class Solution:
    """
    @param nums: an array of positive and negative integers
    @return: if there is a loop in this array
    """
    def circularArrayLoop(self, nums):
        n = len(nums)
        if n < 2:
            return False

        for i in range(n):
            if nums[i] == 0:
                continue

            sign = nums[i] / abs(nums[i])
            slow = self.move(nums, n, i, 1, sign)
            fast = self.move(nums, n, i, 2, sign)

            while fast != -1 and fast != slow:
                fast = self.move(nums, n, fast, 2, sign)
                slow = self.move(nums, n, slow, 1, sign)

            if fast != -1 and nums[fast] % n > 0:
                return True

        return False


    def move(self, nums, n, i, times, sign):
        for _ in range(times):
            i += nums[i]
            i %= n
            if nums[i] * sign < 0:
                return -1
        return i