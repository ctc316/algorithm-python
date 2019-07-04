class Solution:
    """
    @param grid: the 2D grid
    @return: the shortest distance
    """
    def shortestDistance(self, grid):
        if not grid:
            return -1

        self.EMPTY = 0
        self.HOUSE = 1
        self.WALL = 2
        self.MOVES = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        self.grid = grid
        self.n = len(grid)
        self.m = len(grid[0])
        self.distances = [[0 for _ in range(self.m)] for _ in range(self.n)]
        self.reached = [[0 for _ in range(self.m)] for _ in range(self.n)]

        house_cnt = 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == self.HOUSE:
                    self.bfsFromHouse(i, j)
                    house_cnt += 1

        min_dist = float("Inf")
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] != self.EMPTY or self.reached[i][j] != house_cnt:
                    continue
                min_dist = min(min_dist, self.distances[i][j])

        return min_dist


    def bfsFromHouse(self, i, j):
        from queue import Queue
        q = Queue()
        visited = [[False for _ in range(self.m)] for _ in range(self.n)]

        q.put((i, j))
        dist = 0

        while not q.empty():
            for _ in range(q.qsize()):
                x, y = q.get()
                self.distances[x][y] += dist
                self.reached[x][y] += 1

                for move in self.MOVES:
                    x_ = x + move[0]
                    y_ = y + move[1]

                    if x_ < 0 or x_ >= self.n or y_ < 0 or y_ >= self.m or \
                       visited[x_][y_] or self.grid[x_][y_] != self.EMPTY:
                        continue

                    visited[x_][y_] = True
                    q.put((x_, y_))

            dist += 1
