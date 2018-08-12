class NumMatrix:
    """
    @param: matrix: a 2D matrix
    """
    def __init__(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return

        n = len(matrix)
        m = len(matrix[0])
        self.presum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                self.presum[i + 1][j + 1] = matrix[i][j] + self.presum[i + 1][j] + self.presum[i][j + 1] - self.presum[i][j]


    """
    @param: row1: An integer
    @param: col1: An integer
    @param: row2: An integer
    @param: col2: An integer
    @return: An integer
    """
    def sumRegion(self, row1, col1, row2, col2):
        return self.presum[row2 + 1][col2 + 1] - self.presum[row1][col2 + 1] - self.presum[row2 + 1][col1] + self.presum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)