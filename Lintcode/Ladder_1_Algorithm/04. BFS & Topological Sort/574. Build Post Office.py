# Version 1: BFS for all cell, (Time Limit Exceed)
from queue import Queue

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Solution:
    EMPTY = 0
    HOUSE = 1
    MOVE = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    minDist = sys.maxsize
    houseNum = 0
    n = 0
    m = 0

    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        if len(grid) == 0:
            return -1

        self.minDist = sys.maxsize
        self.houseNum = 0
        self.n = len(grid)
        self.m = len(grid[0])

        # count houses
        for i in range(self.n):
           for j in range(self.m):
               if grid[i][j] == self.HOUSE:
                   self.houseNum += 1

        if self.houseNum == 0:
            return 0

        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == self.EMPTY:
                    self.bfs(grid, i, j)

        return self.minDist



    def bfs(self, grid, x, y):
        q = Queue()
        visited = [[False for j in range(self.m)] for i in range(self.n)]

        q.put(Pair(x, y))
        visited[x][y] = True

        houseReached = 0
        distSum = 0
        dist = 0
        while not q.empty():
            for i in range(q.qsize()):
                pos = q.get()
                # check is house
                if grid[pos.x][pos.y] == 1:
                    houseReached += 1
                    distSum += dist

                # find next step
                for next in self.findNext(grid, pos.x, pos.y):
                    if visited[next.x][next.y] is True:
                        continue

                    visited[next.x][next.y] = True
                    q.put(next)

            dist += 1

        if houseReached == self.houseNum and distSum < self.minDist:
            self.minDist = distSum



    def findNext(self, grid, x, y):
        results = []
        for i in range(len(self.MOVE)):
            x_ = x + self.MOVE[i][0]
            y_ = y + self.MOVE[i][1]

            if x_ < 0 or x_ >= self.n or y_ < 0 or y_ >= self.m:
                continue

            results.append(Pair(x_, y_))

        return results



#Version 2: BFS from houses, (Time Limit Exceed)
from queue import Queue

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Stat:
    def __init__(self, houseReached, totalDist):
        self.houseReached = houseReached
        self.totalDist = totalDist


class Solution:
    EMPTY = 0
    HOUSE = 1
    MOVE = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    n = 0
    m = 0

    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        if len(grid) == 0:
            return -1

        self.n = len(grid)
        self.m = len(grid[0])

        # BFS from houses
        cellStats = [[Stat(0, 0) for j in range(self.m)] for i in range(self.n)]
        houseNum = 0
        for i in range(self.n):
           for j in range(self.m):
               if grid[i][j] == self.HOUSE:
                   houseNum += 1
                   self.bfs(grid, i, j, cellStats)

        if houseNum == 0:
            return 0

        minDist = sys.maxsize
        for i in range(self.n):
           for j in range(self.m):
               cell = cellStats[i][j]
               if cell.houseReached == houseNum and cell.totalDist < minDist:
                   minDist = cell.totalDist

        return minDist



    def bfs(self, grid, x, y, stats):
        q = Queue()
        visited = [[False for j in range(self.m)] for i in range(self.n)]

        q.put(Pos(x, y))
        visited[x][y] = True

        houseReached = 0
        dist = 0
        while not q.empty():
            for i in range(q.qsize()):
                pos = q.get()
                # count for empty cell
                if grid[pos.x][pos.y] == self.EMPTY:
                    stats[pos.x][pos.y].houseReached += 1
                    stats[pos.x][pos.y].totalDist += dist

                # find next step
                for next in self.findNext(grid, pos.x, pos.y):
                    if visited[next.x][next.y] is True:
                        continue

                    visited[next.x][next.y] = True
                    q.put(next)

            dist += 1



    def findNext(self, grid, x, y):
        results = []
        for i in range(len(self.MOVE)):
            x_ = x + self.MOVE[i][0]
            y_ = y + self.MOVE[i][1]

            if x_ < 0 or x_ >= self.n or y_ < 0 or y_ >= self.m:
                continue

            results.append(Pos(x_, y_))

        return results



# Version 2: calculate distance in the way of seperating x, y 
# since "You can pass through house and empty.""

from queue import Queue

class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1
        
        n = len(grid)
        m = len(grid[0])
        
        # Idea: the dists to a house can be separated to x dist and y dist
        
        # count the houses on each cell in row and col
        rowCount = [0 for i in range(n)]
        colCount = [0 for j in range(m)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rowCount[i] += 1
                    colCount[j] += 1
          
        # calcualte dist sum for rows and cols          
        rowDistSum = [0 for i in range(n)]
        colDistSum = [0 for j in range(m)]
        for row1 in range(n):
            for row2 in range(n):
                rowDistSum[row1] += rowCount[row2] * abs(row2 - row1)
        for col1 in range(m):
            for col2 in range(m):
                colDistSum[col1] += colCount[col2] * abs(col2 - col1)
                
            
        # compare and find min
        minDist = sys.maxsize
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    minDist = min(minDist, rowDistSum[i] + colDistSum[j])
        
        return minDist