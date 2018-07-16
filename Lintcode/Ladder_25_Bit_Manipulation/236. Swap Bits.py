class Solution:
    """
    @param: x: An integer
    @return: An integer
    """
    def swapOddEvenBits(self, x):
        '''
        0111  ->  1011
        >> 1:  0011
                ^ ^    <-   mask: 0101 = 0x55555555
        << 1:  1110
               ^ ^     <-   mask: 1010 = 0xAAAAAAAA
        '''

        return (x >> 1) & 0x55555555 | (x << 1) & 0xAAAAAAAA