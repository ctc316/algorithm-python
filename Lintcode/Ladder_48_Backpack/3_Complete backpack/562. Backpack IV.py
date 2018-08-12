class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackIV(self, nums, target):
        '''
            [2,3,6,7]
            7
             0       4     7
            [1,0,0,0,0,0,0,0]
          2 [1,0,1,0,1,0,1,0]
          3 [1,0,1,1,1,1,1,1]
          6 [1,0,1,1,1,1,2,1]
          7 [1,0,1,1,1,1,2,2]
        '''

        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for num in nums:
            for j in range(num, target + 1):
                dp[j] += dp[j - num]

        return dp[target]