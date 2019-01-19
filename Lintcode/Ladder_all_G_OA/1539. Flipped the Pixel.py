class Solution:
    """
    @param Byte:
    @return: return the answer after flipped
    """
    def flippedByte(self, Byte):
        for i in range(len(Byte)):
           Byte[i] = [0 if bit == 1 else 1 for bit in reversed(Byte[i])]

        return Byte


        # return [[0 if bit == 1 else 1 for bit in reversed(Byte[i])] for i in range(len(Byte))]