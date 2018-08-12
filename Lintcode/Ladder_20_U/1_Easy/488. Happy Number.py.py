class Solution:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    """
    def isHappy(self, n):
        hash = set()
        while n != 1:
            result = 0
            while n > 0:
                result += pow(n % 10, 2)
                n = int(n / 10)

            n = result
            if n in hash:
                return False
            hash.add(n)

        return True