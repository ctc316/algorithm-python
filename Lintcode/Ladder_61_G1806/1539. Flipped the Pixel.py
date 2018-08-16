class Solution:
    """
    @param Byte:
    @return: return the answer after flipped
    """
    def flippedByte(self, Byte):
        n = len(Byte)
        m = len(Byte[0])
        halfway = int(m / 2)
        for row in Byte:
            for i in range(halfway):
                self.swap(row, i, m - 1 - i)

            for i in range(m):
                row[i] ^= 1

        return Byte


    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp