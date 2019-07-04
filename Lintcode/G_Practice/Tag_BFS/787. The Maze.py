class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def hasPath(self, maze, start, destination):
        '''
        [[0,0,1,0,0],
         [0,0,0,0,0],
         [0,0,0,1,0],
         [1,1,0,1,1],
         [0,0,0,0,0]]
        '''
        if not maze:
            return False

        self.WALL = 1
        self.EMPTY = 0
        DIRECTIONS = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        n = len(maze)
        m = len(maze[0])

        from queue import Queue
        q = Queue()
        visited = set()

        for i in range(len(DIRECTIONS)):
            q.put((start[0], start[1], i))
            visited.add((start[0], start[1], i))

        while not q.empty():
            x, y, dir_idx = q.get()
            x_ = x + DIRECTIONS[dir_idx][0]
            y_ = y + DIRECTIONS[dir_idx][1]
            if self.available(maze, n, m, x_, y_):
                next = (x_, y_, dir_idx)
                if next not in visited:
                    visited.add(next)
                    q.put(next)
            else:
                if x == destination[0] and y == destination[1]:
                    return True
                for i in range(len(DIRECTIONS)):
                    if i == dir_idx:
                        continue
                    x_ = x + DIRECTIONS[i][0]
                    y_ = y + DIRECTIONS[i][1]
                    if self.available(maze, n, m, x_, y_):
                        next = (x_, y_, i)
                        if next not in visited:
                            visited.add(next)
                            q.put(next)

        return False


    def available(self, maze, n, m, x, y):
        return x >= 0 and x < n and y >= 0 and y < m and maze[x][y] != self.WALL