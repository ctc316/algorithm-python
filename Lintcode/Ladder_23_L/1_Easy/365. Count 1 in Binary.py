class Solution:
    """
    @param: num: An integer
    @return: An integer
    """
    def countOnes(self, num):
        count = 0
        if num < 0:
            num &= 0xFFFFFFFF

        while num != 0:
            count += 1
            num &= num - 1

        return count