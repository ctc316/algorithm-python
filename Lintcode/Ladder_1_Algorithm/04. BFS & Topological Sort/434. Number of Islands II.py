# Version 1: use BFS to explore and find connected Island from each operator, TIME LIMIT EXCEED

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

from queue import Queue

class Solution:

    SEA = 0
    ISLAND = 1
    ADJACENT = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        if n < 1 or m < 1 or len(operators) == 0:
            return []

        islands = 0
        results = [0 for i in range(len(operators))]
        matrix = [[self.SEA for j in range(m)] for i in range(n)]
        for i in range(len(operators)):
            op = operators[i]
            if matrix[op.x][op.y] is self.ISLAND:
                continue

            matrix[op.x][op.y] = self.ISLAND
            islands += 1
            islands = self.explore(matrix, n, m, op, islands)
            results[i] = islands

        return results


    def explore(self, matrix, n, m , op, islands):
        visited = [[False for j in range(m)] for i in range(n)]
        visited[op.x][op.y] = True

        q = Queue()

        for start in self.getNear(n, m, op):
            if matrix[start.x][start.y] == self.SEA or \
               visited[start.x][start.y] is True:
                    continue

            islands -= 1
            visited[start.x][start.y] = True
            q.put(start)

            while not q.empty():
                for next in self.getNear(n, m, q.get()):
                    if matrix[next.x][next.y] == self.SEA or \
                       visited[next.x][next.y] is True:
                        continue

                    visited[next.x][next.y] = True
                    q.put(next)

        return islands


    def getNear(self, n, m, pt):
        results = []
        for adj in self.ADJACENT:
            x_ = pt.x + adj[0]
            y_ = pt.y + adj[1]

            if x_ < 0 or x_ >= n or y_ < 0 or y_ >= m:
                continue

            results.append(Point(x_, y_))

        return results



# Version 2: Union Find Set
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class UnionFind:
    def __init__(self, n, m):
        self.father = [i for i in range(n * m)]
        self.n = n
        self.m = m


    def find(self, x, y):
        # find root father
        root = self.father[self.convertToId(x, y)]
        while root != self.father[root]:
            root = self.father[root]

        # compress
        temp = -1
        pointer = self.convertToId(x, y)
        while pointer != self.father[pointer]:
            temp = self.father[pointer]
            self.father[pointer] = root
            pointer = temp

        return root


    def union(self, x1, y1, x2, y2):
        fa1 = self.find(x1, y1)
        fa2 = self.find(x2, y2)
        if fa1 != fa2:
            self.father[fa1] = fa2


    def convertToId(self, x, y):
        return x * self.m + y


class Solution:

    ADJACENT = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        k = len(operators)
        if n < 1 or m < 1 or k == 0:
            return []

        uf = UnionFind(n, m)
        islands = 0
        placed = [[False for j in range(m)] for i in range(n)]
        results = [0 for i in range(k)]

        for i in range(k):
            x = operators[i].x
            y = operators[i].y

            if not placed[x][y]:
                placed[x][y] = True
                islands += 1
                for adj in self.ADJACENT:
                    x_ = x + adj[0]
                    y_ = y + adj[1]
                    if x_ < 0 or x_ >= n or y_ < 0 or y_ >= m or not placed[x_][y_]:
                        continue

                    fa = uf.find(x, y)
                    fa_ = uf.find(x_, y_)

                    if fa != fa_:
                        islands -= 1
                        uf.union(x, y, x_, y_)

            results[i] = islands

        return results