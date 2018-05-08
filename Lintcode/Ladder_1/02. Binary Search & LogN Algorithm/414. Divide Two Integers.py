class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        if divisor == 0:
            return 2147483647

        isNegative = False
        if divisor < 0:
            isNegative = True
            divisor = -divisor

        if dividend < 0:
            isNegative = not isNegative
            dividend = -dividend


        start = 0
        end = dividend
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if mid * divisor < dividend:
                start = mid
            else:
                end = mid


        ans = end
        if end * divisor > dividend:
            ans = start

        if isNegative:
            ans = -ans

        if ans > 2147483647:
            ans = 2147483647

        return ans


# Version 2: using bit shift
class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        INT_MAX = 2147483647
        
        if divisor == 0:
            return INT_MAX
        
        neg = dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0
        a, b = abs(dividend), abs(divisor)
        
        ans, shift = 0, 31
        while shift >= 0:
            if a >= b << shift:
                a -= b << shift
                ans += 1 << shift
            shift -= 1
            
        if neg:
            ans = - ans
        
        if ans > INT_MAX:
            return INT_MAX
        
        return ans