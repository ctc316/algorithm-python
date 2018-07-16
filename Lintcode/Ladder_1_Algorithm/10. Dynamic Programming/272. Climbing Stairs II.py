class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climbStairs2(self, n):
        '''
           0 1 2 3
           1 1 2 4
        '''
        counts = [0 for i in range(n + 1)]
        counts[0] = 1
        for i in range(1, n + 1):
            for step in range(1, 4):
                if i - step >= 0:
                    counts[i] += counts[i - step]

        return counts[n]