# Version 1: prefix sum, Time: O(n^2), Space: O(n), Time Limit Exceeded
class Solution:
    """
    @param: nums: an array with positive and negative numbers
    @param: k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        if len(nums) < k:
            return 0

        n = len(nums)

        """
        prefixSum[i + j] - prefixSum[i] == sum of nums[i] ~ nums[j]

           [1, 12, -5, -6, 50,  3]
        [0, 1, 13,  8,  2, 52, 55]
        """

        preSum = [0 for i in range(n + 1)]
        sum = 0
        for i in range(n):
            sum += nums[i]
            preSum[i + 1] = sum

        maxAvg = -sys.maxsize - 1
        for i in range(0, n + 1 - k):
            for j in range(i + k, n + 1):
                avg = (preSum[j] - preSum[i]) / (j - i)
                if avg > maxAvg:
                    maxAvg = avg

        return maxAvg



# Version 2: Binary Search, Time: O(nlogn), Space: O(n)
class Solution:
    """
    @param: nums: an array with positive and negative numbers
    @param: k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        if len(nums) < k:
            return 0

        n = len(nums)
        start = -1e12
        end = 1e12
        eps = 1e-6

        # Looking for the range of nums (Optional)
        # for i in range(n):
        #     start = min(start, nums[i])
        #     end = max(end, nums[i])

        while start + eps < end:
            mid = start + (end - start) / 2
            if self.check(nums, mid, k):
                start = mid
            else:
                end = mid

        return end;


    def check(self, nums, mid, k):
        n = len(nums)
        diffSum = [0 for i in range(n + 1)]
        pre_min = [0 for i in range(n + 1)]

        for i in range(1, n + 1):
            diffSum[i] = diffSum[i - 1] + (nums[i - 1] - mid)
            pre_min[i] = min(pre_min[i - 1], diffSum[i])

            if i >= k and diffSum[i] - pre_min[i - k] >= 0:
                return True;

        return False



# Version 3: Binary Search, Time: O(nlogn), Space: O(1)
class Solution:
    """
    @param: nums: an array with positive and negative numbers
    @param: k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        if len(nums) < k:
            return 0
            
        n = len(nums)
        start = -1e10
        end = 1e10
        eps = 1e-5
        
        # Looking for the range of nums (Optional)
        for i in range(n): 
            start = min(start, nums[i])
            end = max(end, nums[i])
            
        while start + eps < end:
            mid = start + (end - start) / 2
            if self.check(nums, mid, k):
                start = mid
            else:
                end = mid
        
        return end;
        
        
    def check(self, nums, mid, k):
        totalDiffSum = 0
        prevDiffSum = 0 
        minSum = sys.maxsize
        
        for i in range(0, len(nums)):
            totalDiffSum += nums[i] - mid;
            if i >= k - 1 and totalDiffSum >= 0 :
                return True;
    
            if i >= k:
                prevDiffSum += nums[i - k] - mid
                minSum = min(minSum, prevDiffSum)
                if totalDiffSum - minSum >= 0:
                    return True

        return False