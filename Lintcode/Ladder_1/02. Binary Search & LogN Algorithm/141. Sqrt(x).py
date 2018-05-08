# Version 1: Brute Force, Time: O(n)
class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        n = 0
        while n * n <= x:
            n += 1
            
        return n - 1
        

#Version 2: Binary Search, Time: O(logn)
class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        if x <= 1: 
            return x
            
        start, end = 1, x
        while start + 1 < end:
            mid = start + int((end - start) / 2)
            sqr = mid * mid
            if sqr < x:
                start = mid
            elif sqr > x:
                end = mid
            else:
                return mid
                
        if end * end <= x:
            return end
        return start