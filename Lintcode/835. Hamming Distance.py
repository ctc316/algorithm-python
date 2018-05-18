class Solution:
    """
    @param x: an integer
    @param y: an integer
    @return: return an integer, denote the Hamming Distance between two integers
    """
    def hammingDistance(self, x, y):
        '''
        0001
        0100  -> 3
        '''

        xor = x ^ y
        count = 0
        while xor > 0:
            if xor % 2 == 1:
                count += 1
            xor = xor >> 1

        return count