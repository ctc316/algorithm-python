class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return

        self.n = len(matrix)
        self.m = len(matrix[0])
        self.matrix = [[0 for _ in range(self.m)] for _ in range(self.n)]
        self.bitree = [[0 for _ in range(self.m + 1)] for _ in range(self.n + 1)]

        for i in range(self.n):
            for j in range(self.m):
                self.update(i, j, matrix[i][j])


    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """

        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val

        row += 1
        col += 1
        while row <= self.n:
            c = col
            while c <= self.m:
                self.bitree[row][c] += diff
                c += c & (-c)

            row += row & (-row)


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        return self._getSum(row2, col2) \
             - self._getSum(row1 - 1, col2) \
             - self._getSum(row2, col1 - 1) \
             + self._getSum(row1 - 1, col1 - 1)


    def _getSum(self, row, col):
        row += 1
        col += 1
        sum = 0
        while row > 0:
            c = col
            while c > 0:
                sum += self.bitree[row][c]
                c -= c & (-c)

            row -= row & (-row)

        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)