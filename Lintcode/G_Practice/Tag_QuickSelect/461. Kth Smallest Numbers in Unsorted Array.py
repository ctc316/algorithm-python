class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        return self.quickSelect(k, nums, 0, len(nums) - 1)

    def quickSelect(self, k, nums, start, end):
        l = start
        r = end
        pivot = nums[l + (r - l) // 2]
        while l <= r:
            while l <= r and nums[l] < pivot:
                l += 1
            while l <= r and nums[r] > pivot:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        k_pos = start + k - 1
        if k_pos <= r:
            return self.quickSelect(k, nums, start, r)
        elif k_pos >= l:
            return self.quickSelect(k_pos - l + 1, nums, l, end)
        else:
            return nums[k_pos]