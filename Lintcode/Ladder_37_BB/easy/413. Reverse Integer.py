class Solution:
    """
    @param n: the integer to be reversed
    @return: the reversed integer
    """
    def reverseInteger(self, n):
        isNeg = n < 0
        if isNeg:
            n = -n
        res = int(str(n)[::-1])
        if res >= 2 ** 32:
            return 0

        if isNeg:
            return res * -1
        return res
