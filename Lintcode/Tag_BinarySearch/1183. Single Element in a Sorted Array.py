class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """
    def singleNonDuplicate(self, nums):
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            mid = l + (r - l) // 2
            p1 = p2 = mid
            if mid > 0 and nums[mid] == nums[mid - 1]:
                p1 = mid - 1
            elif mid < n - 1 and nums[mid] == nums[mid + 1]:
                p2 = mid + 1
            else:
                return nums[mid]

            if (p1 - l) % 2 == 1:
                r = p1 - 1
            else:
                l = p2 + 1

        return nums[l]