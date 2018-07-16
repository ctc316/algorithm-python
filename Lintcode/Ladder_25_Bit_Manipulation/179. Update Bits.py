class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param i: A bit position
    @param j: A bit position
    @return: An integer
    """
    def updateBits(self, n, m, i, j):
        '''
        n = (00000000000000000000010000000000)2
        m = (00000000000000000000000000010101)2

        處理 n:
           1) mod = -1 << (31 - j) = (11111110000000000000000000000000)2
           2) mod = mod >>> (31 - j + i) = (00000000000000000000000000011111)2
           3) mod = mod << i
           4) mod = ~mod
           5) n = n & mod

        處理 m:
           m << i
        '''

        '''
        00000000000000000000001111101001  n=1001
                                ^^^^^^
                                011110    m=30

        11111111111111111111111110000000  hi=-128
        00000000000000000000000000000011  lo=   3
        11111111111111111111111110000011   -125

        '''

        if j == 31:
            higherBitsMask = 0
        else:
            higherBitsMask = ~((1 << (j + 1)) - 1)

        lowerBitsMask = (1 << i) - 1
        clearMask = higherBitsMask | lowerBitsMask

        # pos = '033b'
        # print(format(higherBitsMask, pos), higherBitsMask)
        # print(format(lowerBitsMask, pos), lowerBitsMask)
        # print(format(clearMask, pos), clearMask)
        # print(format(n, pos), n)
        # print(format(clearMask & n, pos),  clearMask & n)
        # print(format(m, pos))
        # print(format(m << i, pos))
        # print(format((clearMask & n) | (m << i), pos))
        # print(0x7fffffff)

        result = (clearMask & n) | (m << i)
        if result > 0x7fffffff:
            result = (-0x7fffffff - 1) | (result & 0x7fffffff)

        return result