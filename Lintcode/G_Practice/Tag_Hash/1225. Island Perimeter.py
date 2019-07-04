class Solution:
    """
    @param grid: a 2D array
    @return: the perimeter of the island
    """
    def islandPerimeter(self, grid):
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        n = len(grid)
        m = len(grid[0])
        perimeter = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                perimeter += 4
                for adj in [[-1, 0], [0, -1]]:
                    x = i + adj[0]
                    y = j + adj[1]
                    if x >= 0 and x < n and y >= 0 and y < m and grid[x][y] == 1:
                        perimeter -= 2

        return perimeter