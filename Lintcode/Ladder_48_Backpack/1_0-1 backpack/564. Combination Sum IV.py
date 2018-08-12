class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackVI(self, nums, target):
        '''
            [1,2,4]
            4

            [1,0,0,0,0]
            [1,1,0,0,0]
            [1,1,2,0,0]
            [1,1,2,3,0]
            [1,1,2,3,6]
        '''

        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]

        return dp[target]