class Solution:
    """
    @param targetMap:
    @return: nothing
    """
    def shortestPath(self, targetMap):
        n = len(targetMap)
        m = len(targetMap[0])

        from queue import Queue
        q = Queue()
        q.put((0, 0))

        visited = [[False for _ in range(m)] for __ in range(n)]
        visited[0][0] = True

        steps = -1
        while not q.empty():
            steps += 1
            for _ in range(q.qsize()):
                x, y = q.get()

                if targetMap[x][y] == 2:
                    return steps

                for move in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    x_ = x + move[0]
                    y_ = y + move[1]

                    if x_ < 0 or x_ >= n or y_ < 0 or y_ >= m or targetMap[x_][y_] == 1 or visited[x_][y_]:
                        continue

                    q.put((x_, y_))
                    visited[x_][y_] = True

        return -1