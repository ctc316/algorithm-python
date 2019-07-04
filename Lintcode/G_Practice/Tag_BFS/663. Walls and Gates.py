class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        if not rooms:
            return

        WALL = -1
        GATE = 0
        INF = 2147483647

        n = len(rooms)
        m = len(rooms[0])

        from queue import Queue
        q = Queue()
        visited = [[False for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if rooms[i][j] == GATE:
                    q.put((i, j))
                    visited[i][j] = True

        distance = 0
        while not q.empty():
            for _ in range(q.qsize()):
                x, y = q.get()
                rooms[x][y] = min(rooms[x][y], distance)
                for adj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    x_ = x + adj[0]
                    y_ = y + adj[1]
                    if x_ < 0 or x_ >= n or y_ < 0 or y_ >= m or \
                       rooms[x_][y_] == WALL or visited[x_][y_]:
                        continue

                    visited[x_][y_] = True
                    q.put((x_, y_))

            distance += 1