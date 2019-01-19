class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        n = len(heights)
        if n < 3:
            return 0

        left_max = [0 for _ in range(n)]
        for i in range(1, n):
            left_max[i] = max(heights[i - 1], left_max[i - 1])

        right_max = 0
        summ = 0;
        for i in range(n - 2, -1, -1):
            right_max = max(right_max, heights[i + 1])
            water = min(left_max[i], right_max) - heights[i]
            if water > 0:
                summ += water

        return summ



'''
变体(-1 表示漏水， V存的⽔都能漏下)
[3, 1,-1, 2, 1,2] 结果为1， [2,1,2] subarray 可以存⽔
[3, 1, 1, 2, 1,2] 结果为3，subarray [3, 1, 1, 2] [2,1,2] 都可以存⽔
'''

class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        n = len(heights)
        if n < 3:
            return 0

        left_max = [0 for _ in range(n)]
        for i in range(1, n):
            if heights[i] == -1:
                left_max[i] = -1
            elif left_max[i - 1] == -1 and heights[i - 1] <= heights[i]:
                left_max[i] = -1
            else:
                left_max[i] = max(heights[i - 1], left_max[i - 1])
        
        right_max = 0
        summ = 0;
        for i in range(n - 2, -1, -1):
            if heights[i] == -1:
                right_max = -1
            elif right_max == -1 and heights[i + 1] <= heights[i]:
                right_max = -1
            else:
                right_max = max(heights[i + 1], right_max)
            
            water = min(left_max[i], right_max) - heights[i]
            if water > 0:
                summ += water
                
        return summ