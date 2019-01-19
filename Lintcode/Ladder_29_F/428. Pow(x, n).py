class Solution:
    """
    @param x: the base number
    @param n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        negative = False
        if n < 0:
            negative = True
            n = -n

        ans = 1
        while n > 0:
            times = 1
            multiply = x
            while times * 2 < n:
                times *= 2
                multiply *= multiply

            n -= times
            ans *= multiply

        if negative:
            return 1 / ans
        return ans