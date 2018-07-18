# Version 1: DP, Time: O(n * m)
class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
            
        n = len(grid)
        m = len(grid[0])
        
        up = [[0 for _ in range(m)] for __ in range(n)]
        down = [[0 for _ in range(m)] for __ in range(n)]
        left = [[0 for _ in range(m)] for __ in range(n)]
        right = [[0 for _ in range(m)] for __ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'W':
                    continue
                if grid[i][j] == "E":
                    up[i][j] = 1
                if i - 1 >= 0:
                    up[i][j] += up[i - 1][j]
        
        for i in range(n - 1, -1, -1):
            for j in range(m):
                if grid[i][j] == 'W':
                    continue
                if grid[i][j] == "E":
                    down[i][j] = 1
                if i + 1 < n:
                    down[i][j] += down[i + 1][j]
                    
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'W':
                    continue
                if grid[i][j] == "E":
                    left[i][j] = 1
                if j - 1 >= 0:
                    left[i][j] += left[i][j - 1]
        
        for i in range(n):
            for j in range(m - 1, -1, -1):
                if grid[i][j] == 'W':
                    continue
                if grid[i][j] == "E":
                    right[i][j] = 1
                if j + 1 < m:
                    right[i][j] += right[i][j + 1]
                    
        maximum = 0 
        for i in range(n):
            for j in range(m):
                if grid[i][j] != "0":
                    continue
                maximum = max(maximum, up[i][j] + down[i][j] + left[i][j] + right[i][j])
        
        return maximum



# Version 2: BFS, Time: O(n * m * (n + m)), TLE
class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
            
        n = len(grid)
        m = len(grid[0])
        
        counts = [[0 for _ in range(m)] for __ in range(n)]
        MOVES = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 'E':
                    continue
        
                for move in MOVES:
                    x = i + move[0]
                    y = j + move[1]
                    while x >= 0 and x < n and y >= 0 and y < m and grid[x][y] != "W":
                        counts[x][y] += 1
                        x += move[0]
                        y += move[1]
                    
        maximum = 0 
        for i in range(n):
            for j in range(m): 
                maximum = max(maximum, counts[i][j])
        
        return maximum