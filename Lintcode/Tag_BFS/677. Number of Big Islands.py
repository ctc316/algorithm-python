class Solution:
    """
    @param grid: a 2d boolean array
    @param k: an integer
    @return: the number of Islands
    """
    def numsofIsland(self, grid, k):
        self.n = len(grid)
        self.m = len(grid[0])
        self.MOVES = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        visited = [[False for _ in range(self.m)] for __ in range(self.n)]
        ans = 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 0 or visited[i][j]:
                    continue

                visited[i][j] = True
                ans += self.bfs(grid, k, visited, i, j)

        return ans


    def bfs(self, grid, k, visited, x, y):
        from queue import Queue
        q = Queue()
        q.put((x, y))
        size = 0
        while not q.empty():
            size += 1
            x, y = q.get()
            for move in self.MOVES:
                x_ = x + move[0]
                y_ = y + move[1]
                if x_ < 0 or x_ >= self.n or y_ < 0 or y_ >= self.m  \
                  or visited[x_][y_] or grid[x_][y_] == 0:
                    continue

                visited[x_][y_] = True
                q.put((x_, y_))

        return 0 if size < k else 1