class Solution:
    """
    @param n: an integer
    @return: the number of solutions
    """
    def threeSum2(self, n):
        res = 0
        for z in range(0, int(n ** 0.5) + 1):
            x, y = 0, z
            target = n - z ** 2
            while x <= y:
                summ = x ** 2 + y ** 2
                if summ > target:
                    y -= 1
                elif summ < target:
                    x += 1
                else:
                    y -= 1
                    res += 1

        return res