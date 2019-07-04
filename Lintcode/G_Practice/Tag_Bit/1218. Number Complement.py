class Solution:
    """
    @param num: an integer
    @return: the complement number
    """
    def findComplement(self, num):
        '''
        5  0101
           0111
        ^  1010  不同變為 1
        '''

        return num ^ ((1 << num.bit_length()) - 1)