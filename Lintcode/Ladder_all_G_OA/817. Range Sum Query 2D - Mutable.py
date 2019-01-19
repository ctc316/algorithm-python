class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.n = len(matrix)
        self.m = 0 if self.n == 0 else len(matrix[0])
        self.matrix = [[0 for _ in range(self.m)] for __ in range(self.n)]
        self.BITree = [[0 for _ in range(self.m + 1)] for __ in range(self.n + 1)]

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

        i = row + 1
        while i <= self.n:
            j = col + 1
            while j <= self.m:
                self.BITree[i][j] += diff
                j += j & -j

            i += i & -i


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.prefixSum(row2, col2) - \
               self.prefixSum(row2, col1 - 1) - \
               self.prefixSum(row1 - 1, col2) + \
               self.prefixSum(row1 - 1, col1 - 1)


    def prefixSum(self, row, col):
        summ = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                summ += self.BITree[i][j]
                j -= j & -j

            i -= i & -i

        return summ


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)