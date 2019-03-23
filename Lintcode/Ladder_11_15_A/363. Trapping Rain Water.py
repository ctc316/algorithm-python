class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        n = len(heights)
        if n < 3:
            return 0

        l, r = 0, n - 1
        l_max, r_max = 0, 0
        total = 0
        while l <= r:
            if l_max < r_max:
                total += max(0, min(l_max, r_max) - heights[l])
                l_max = max(l_max, heights[l])
                l += 1
            else:
                total += max(0, min(l_max, r_max) - heights[r])
                r_max = max(r_max, heights[r])
                r -= 1

        return total