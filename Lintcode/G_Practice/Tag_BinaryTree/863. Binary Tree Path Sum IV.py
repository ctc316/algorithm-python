class Solution:
    """
    @param nums: a list of integers
    @return: return an integer
    """
    def pathSum(self, nums):
        '''
        [113, 215, 221, 312, 334]
            3
          5   1
        2    4

        [115,213,227,336,345]
            5
          3   7
             6  5
        '''
        summ = 0
        carrys = [[0 for i in range(8)] for _ in range(4)]
        for num in nums[::-1]:
            layer = num // 100 - 1
            pos = ((num % 100) // 10) - 1
            val = num % 10
            if carrys[layer][pos] < 2:
                summ += val
            else:
                summ += val * carrys[layer][pos]
            carrys[layer - 1][pos // 2] += 1 if carrys[layer][pos] == 0 else carrys[layer][pos]

        return summ