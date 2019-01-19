class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n + 2)]

    def find(self, a):
        path = []
        while self.parent[a] != a:
            path.append(a)
            a = self.parent[a]

        for p in path:
            self.parent[p] = a

        return a

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parent[root_b] = root_a

class Solution:
    """
    @param L: the length
    @param W: the width
    @param p:  the obstacle coordinates
    @return: yes or no
    """
    def drivingProblem(self, L, W, p):
        n = len(p)
        union = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                dx = (p[i][0] - p[j][0]) ** 2
                dy = (p[i][1] - p[j][1]) ** 2
                if dx + dy <= 36:
                    union.union(i, j)

            if p[i][1] <= 5:
                union.union(i, n)

            if W - p[i][1] <= 5:
                union.union(i, n + 1)

        return "no" if union.find(n) == union.find(n + 1) else "yes"









class Solution:
    """
    @param L: the length
    @param W: the width
    @param p:  the obstacle coordinates
    @return: yes or no
    """
    def drivingProblem(self, L, W, p):
        '''
         [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        '''
        self.n = L + 1
        self.m = W + 1
        obstacles = self.buildObstacles(p)
        visited = [[0 for _ in range(self.m)] for __ in range(self.n)]

        from queue import Queue
        q = Queue()

        for j in range(self.m):
            if self.isValidPosition(obstacles, 0, j):
                q.put((0, j))
                visited[0][j] = 1

        while not q.empty():
            x, y = q.get()
            print(x, y)
            if x == L:
                return 'yes'

            for x_, y_ in self.getNextPos(obstacles, x, y):
                if visited[x_][y_]:
                    continue
                visited[x_][y_] = 1

                if not self.isValidPosition(obstacles, x_, y_):
                    continue

                q.put((x_, y_))

        return 'no'


    def buildObstacles(self, positions):
        obstacles = [[0 for _ in range(self.m)] for __ in range(self.n)]
        for x, y in positions:
            obstacles[x][y] = 1
            for radius in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
                x_ = x + radius[0]
                y_ = y + radius[1]

                if x_ < 0 or x_ >= self.n or y_ < 0 or y_ >= self.m:
                    continue

                obstacles[x_][y_] = 1

        return obstacles


    def isValidPosition(self, obstacles, x, y):
        for radius in [[2, 0], [0, 2], [-2, 0], [0, -2], [1, 1], [1, -1], [-1, -1], [-1, 1]]:
            x_ = x + radius[0]
            y_ = y + radius[1]

            if y_ < 0 or y_ >= self.m or (x_ >= 0 and x_ < self.n and obstacles[x_][y_]):
                return False

        return obstacles[x][y] == 0


    def getNextPos(self, obstacles, x, y):
        res = []
        for move in [[1, 0], [0, 1], [0, -1]]:
            x_ = x + move[0]
            y_ = y + move[1]

            if x_ >= self.n or y_ < 0 or y_ >= self.m or x_ >= 0 and obstacles[x_][y_]:
                continue

            res.append((x_, y_))

        return res