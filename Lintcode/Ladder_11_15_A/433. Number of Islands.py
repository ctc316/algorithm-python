class Solution:

    MOVES = [[1, 0], [0, 1], [-1, 0], [0, -1]]


    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        self.n = len(grid)
        if self.n == 0: return 0
        self.m = len(grid[0])
        if self.m == 0: return 0

        self.grid = grid
        self.visited = [[False for _ in range(self.m)] for __ in range(self.n)]

        cnt = 0
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == 0 or self.visited[i][j]:
                    continue
                cnt += 1
                self.__BFS(i, j)

        return cnt


    def __BFS(self, x, y):
        from queue import Queue
        q = Queue()
        q.put((x, y))

        while not q.empty():
            cur_x, cur_y = q.get()
            for next in self.__nextSteps(cur_x, cur_y):
                q.put(next)
                self.visited[next[0]][next[1]] = True


    def __nextSteps(self, x, y):
        res = []
        for m in self.MOVES:
            x_, y_ = x + m[0], y + m[1]

            if x_ < 0 or x_ >= self.n or y_ < 0 or y_ >= self.m:
                continue

            if self.grid[x_][y_] == 0 or self.visited[x_][y_]:
                continue

            res.append((x_, y_))

        return res
