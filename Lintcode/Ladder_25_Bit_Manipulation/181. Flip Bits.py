class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: An integer
    """
    def bitSwapRequired(self, a, b):
        num = a ^ b
        count = 0

        if num < 0:
            num &= 0xFFFFFFFF

        while num != 0:
            num &= num - 1
            count += 1

        return count