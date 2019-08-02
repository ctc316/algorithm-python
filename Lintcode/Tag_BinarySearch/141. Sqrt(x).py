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
            if mid ** 2 > x:
                end = mid
            else:
                start = mid

        return end if end ** 2 <= x else start