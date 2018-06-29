class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1

        n = len(grid)
        m = len(grid[0])
        MOVES = [[1, 2], [-1, 2], [2, 1], [-2, 1]]

        routes = [[sys.maxsize for _ in range(m)] for _ in range(n)]
        routes[0][0] = 0

        for j in range(m):
            for i in range(n):
                if grid[i][j] == 1:
                    continue

                for move in MOVES:
                    _x = i - move[0]
                    _y = j - move[1]

                    if _x < 0 or _x >= n or _y < 0 or _y >= m:
                        continue

                    if routes[_x][_y] == sys.maxsize:
                        continue

                    routes[i][j] = min(routes[i][j], routes[_x][_y] + 1)


        if routes[n - 1][m - 1] == sys.maxsize:
            return -1

        return routes[n - 1][m - 1]