class Solution:
    """
    @param num: a non negative integer number
    @return: an array represent the number of 1's in their binary
    """
    def countBits(self, num):
        '''
        000
        001  <-  000 + 1
        010  <-  000 + 1
        100  <-  000 + 1
        101  <-  100 + 1
        110  <-  100 + 1
        '''

        f = [0 for i in range(num + 1)]
        for i in range(1, num + 1):
            f[i] = f[i & i - 1] + 1

        return f