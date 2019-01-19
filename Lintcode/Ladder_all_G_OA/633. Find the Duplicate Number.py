class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):
        start = 1
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.smaller_than_or_equal_to(nums, mid) > mid:
                end = mid
            else:
                start = mid

        if self.smaller_than_or_equal_to(nums, start) > start:
            return start

        return end

    def smaller_than_or_equal_to(self, nums, val):
        count = 0
        for num in nums:
            if num <= val:
                count += 1
        return count