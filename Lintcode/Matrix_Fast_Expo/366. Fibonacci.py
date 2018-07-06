class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        if n < 2:
            return 0

        i1 = 0
        i2 = 1
        for _ in range(2, n):
            temp = i1 + i2
            i1 = i2
            i2 = temp

        return i2