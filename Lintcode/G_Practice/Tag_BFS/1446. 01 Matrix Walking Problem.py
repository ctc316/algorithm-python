class Solution:
    """
    @param grid: The gird
    @return: Return the steps you need at least
    """
    def getBestRoad(self, grid):
        '''
        [[0,1,0,0,0],
         [0,0,0,1,0],
         [1,1,1,0,0],
         [1,1,1,1,1],
         [1,1,1,0,0]]
        '''
        if not grid:
            return

        WALL = 1
        ROAD = 0

        n = len(grid)
        m = len(grid[0])

        from queue import Queue
        q = Queue()
        visited = set()

        q.put((0, 0, False))
        visited.add((0, 0, False))

        steps = 0
        while not q.empty():
            for _ in range(q.qsize()):
                x, y, turned = q.get()
                if x == n - 1 and y == m - 1:
                    return steps

                for adj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    x_ = x + adj[0]
                    y_ = y + adj[1]
                    if x_ < 0 or x_ >= n or y_ < 0 or y_ >= m or (x_, y_, turned) in visited:
                        continue

                    turn = turned
                    if grid[x_][y_] == WALL:
                        if turn:
                            continue
                        turn = True

                    visited.add((x_, y_, turn))
                    q.put((x_, y_, turn))

            steps += 1

        return -1