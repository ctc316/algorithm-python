class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        start = self.binarySearch(nums, target)
        if start == -1:
            return [-1, -1]
            
        end = self.binarySearch(nums, target, True)
        return [start, end]


    def binarySearch(self, nums, target, getRight=False):
        if len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if nums[mid] == target:
                if getRight:
                    start = mid
                else:
                    end = mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        if getRight:
            if nums[end] == target:
                return end
            elif nums[start] == target:
                return start
        else:
            if nums[start] == target:
                return start
            elif nums[end] == target:
                return end

        return -1