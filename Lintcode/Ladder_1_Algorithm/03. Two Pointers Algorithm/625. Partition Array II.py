class Solution:
    """
    @param: nums: an integer array
    @param: low: An integer
    @param: high: An integer
    @return:
    """
    def partition2(self, nums, low, high):

        left = 0
        right = len(nums) - 1
        mid = 0
        while mid < right:
            if nums[mid] < low:
                self.swap(nums, mid, left)
                left += 1
            if nums[mid] > high:
                self.swap(nums, mid, right)
                right -= 1

            mid += 1



    def swap(self, nums, p1, p2):
        tmp = nums[p1]
        nums[p1] = nums[p2]
        nums[p2] = tmp