class Solution:
    """
    @param n: an integer
    @return: if n is a power of two
    """
    def isPowerOfTwo(self, n):
        # pow of 2 ->  1, 11, 111, 1111, 11111, 111111
        if n < 1:
            return False

        while n > 1:
            if n % 2 != 0:
                return False
            n >>= 1

        return True
