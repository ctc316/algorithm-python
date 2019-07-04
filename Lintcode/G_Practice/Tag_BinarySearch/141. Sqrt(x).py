class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        start = 0
        end = x
        while start + 1.0 < end:
            mid = start + (end - start) // 2
            if mid * mid > x:
                end = mid
            else:
                start = mid

        if end * end <= x:
            return end
        return start