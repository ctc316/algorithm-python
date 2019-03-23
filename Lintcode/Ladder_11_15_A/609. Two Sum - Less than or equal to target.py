class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        n = len(nums)
        if n < 2:
            return 0
            
        nums.sort()
        cnt = 0 
        for i in range(n):
            for j in range(n - 1, i, -1):
                if nums[i] + nums[j] <= target:
                    cnt += j - i
                    break
        
        return cnt