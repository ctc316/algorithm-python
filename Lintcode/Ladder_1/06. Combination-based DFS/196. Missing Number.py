# Version 1: Binary Search, Time: O(nlogn), Space: O(1)
class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def findMissing(self, nums):
        left = 0
        right = len(nums)
        while left + 1 < right:
            mid = left + int((right - left) / 2)
            cnt = self.count(nums, mid)
            if cnt < mid:
                right = mid
            else:
                left = mid

        if self.count(nums, right) == right:
            return right

        return left


    def count(self, nums, mid):
        cnt = 0
        for n in nums:
            if n < mid:
                cnt += 1

        return cnt


# Version 2: Sorting, Time: O(nlogn), Space: O(1)
class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def findMissing(self, nums):
        nums.sort()

        if nums[0] != 0:
            return 0

        for i in range(len(nums) - 1):
            if nums[i] + 1 != nums[i + 1]:
                return nums[i] + 1

        return len(nums)


# Version 3: Sum - every element, Time: O(n), Space: O(1)
class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def findMissing(self, nums):
        n = len(nums)
        sumShouldBe = int(n * (n + 1) / 2)
        for i in nums:
            sumShouldBe -= i

        return sumShouldBe