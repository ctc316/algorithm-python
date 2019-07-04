class Solution:
    """
    @param matrix: the given matrix
    @return: The list of grid coordinates
    """
    def pacificAtlantic(self, matrix):
        pac, atl = set(), set()
        n = len(matrix)
        m = len(matrix[0])
        for i in range(m):
            self.dfs(matrix, n, m, 0, i, pac, 0)
            self.dfs(matrix, n, m, n - 1, i, atl, 0)
        for i in range(n):
            self.dfs(matrix, n, m, i, 0, pac, -1)
            self.dfs(matrix, n, m, i, m - 1, atl, 0)

        return list(pac & atl)


    def dfs(self, matrix, n, m, x, y, water, height):
        if x < 0 or x >= n or y < 0 or y >= m or (x, y) in water or matrix[x][y] < height:
            return

        water.add((x, y))
        self.dfs(matrix, n, m, x - 1, y, water, matrix[x][y])
        self.dfs(matrix, n, m, x + 1, y, water, matrix[x][y])
        self.dfs(matrix, n, m, x, y - 1, water, matrix[x][y])
        self.dfs(matrix, n, m, x, y + 1, water, matrix[x][y])