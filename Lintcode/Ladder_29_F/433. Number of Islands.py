class Solution:
    
    MOVES = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        self.n = len(grid)
        if self.n == 0:
            return 0
    
        self.m = len(grid[0])
        if self.m == 0:
            return 0
        
        visited = [[False for _ in range(self.m)] for __ in range(self.n)]
    
        count = 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 0 or visited[i][j]:
                    continue
    
                count += 1
                self.BFS(grid, visited, i, j)
    
        return count
    
    
    def BFS(self, grid, visited, x, y):
        from queue import Queue
        q = Queue()
        q.put((x, y))
    
        while not q.empty():
            cur_x, cur_y = q.get()
            for next in self.explore(grid, visited, cur_x, cur_y):
                q.put(next)
                visited[next[0]][next[1]] = True
    
    
    def explore(self, grid, visited, x, y):
        result = []
        for move in self.MOVES:
            x_ = x + move[0]
            y_ = y + move[1]
    
            if x_ < 0 or x_ >= self.n or y_ < 0 or y_ >= self.m:
                continue
    
            if grid[x_][y_] == 0 or visited[x_][y_]:
                continue 
    
            result.append((x_, y_))
    
        return result