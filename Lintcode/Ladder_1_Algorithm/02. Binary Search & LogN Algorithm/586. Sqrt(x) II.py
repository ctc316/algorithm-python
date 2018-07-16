class Solution:
    """
    @param: x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
    
        left = 0.0
        right = 1.0 if x < 1.0 else x
        precision = 1e-10

        while(left + precision < right):
            mid = left + (right - left) / 2
            if mid * mid < x:
                left = mid
            else: 
                right = mid

        return left