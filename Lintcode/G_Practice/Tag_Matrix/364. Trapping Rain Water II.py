class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """
    def trapRainWater(self, heights):
        '''
        将矩阵周边的格子都放到堆里，这些格子上面是无法盛水的。
        每次在堆里挑出一个高度最小的格子 cell，把周围的格子加入到堆里。
        这些格子被加入堆的时候，计算他们上面的盛水量。

        盛水量 = cell.height - 这个格子的高度
        当然如果这个值是负数，盛水量就等于 0。
        '''
        if not heights:
            return 0

        self.n = len(heights)
        self.m = len(heights[0])
        self.visited = set()
        borders = []

        from queue import PriorityQueue
        self.pq = PriorityQueue()

        # init with borders
        for i in range(self.n):
            self.add(heights[i][0], i, 0)
            self.add(heights[i][self.m - 1], i, self.m - 1)
        for j in range(1, self.m - 1):
            self.add(heights[0][j], 0, j)
            self.add(heights[self.n - 1][j], self.n - 1, j)

        water = 0
        while not self.pq.empty():
            height, x, y = self.pq.get()
            for x_, y_ in self.adjacent(x, y):
                water += max(0, height - heights[x_][y_])
                self.add(max(height, heights[x_][y_]), x_, y_)

        return water


    def add(self, height, x, y):
        self.pq.put((height, x, y))
        self.visited.add((x, y))

    def adjacent(self, x, y):
        res = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x_ = x + dx
            y_ = y + dy
            if 0 <= x_ < self.n and 0 <= y_ < self.m and (x_, y_) not in self.visited:
                res.append((x_, y_))
        return res