class Solution:
    """
    @param matrix: an integer matrix
    @return: the length of the longest increasing path
    """
    def longestIncreasingPath(self, matrix):
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        n = len(matrix)
        m = len(matrix[0])
        longest = 0
        memory = {}
        for i in range(n):
            for j in range(m):
                longest = max(longest, self.dfs(matrix, n, m, i, j, True, memory))
                longest = max(longest, self.dfs(matrix, n, m, i, j, False, memory))

        return longest


    def dfs(self, matrix, n, m, i, j, ascending, memory):
        memKey = str(i) + "_" + str(j) + "_" + str(ascending)
        if memKey in memory:
            return memory[memKey]

        longest = 0
        for adj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            x = i + adj[0]
            y = j + adj[1]
            if x < 0 or x >= n or y < 0 or y >= m:
                continue
            if ascending and matrix[x][y] <= matrix[i][j]:
                continue
            if not ascending and matrix[x][y] >= matrix[i][j]:
                continue
            longest = max(longest, self.dfs(matrix, n, m, x, y, ascending, memory))

        memory[memKey] = longest + 1
        return memory[memKey]