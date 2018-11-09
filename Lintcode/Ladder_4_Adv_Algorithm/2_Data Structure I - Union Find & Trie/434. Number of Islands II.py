"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class UnionFind:
    def __init__(self, n, m):
        self.parent = [i for i in range(n * m)]
        self.num = 0
        self.n = n
        self.m = m

    def connect(self, p1, p2):
        root_a = self.find(p1)
        root_b = self.find(p2)

        if root_a != root_b:
            self.parent[root_a] = root_b
            self.num -= 1

    def find(self, p):
        a = self.point_to_a(p)
        path = []
        while self.parent[a] != a:
            path.append(a)
            a = self.parent[a]

        for p in path:
            self.parent[p] = a

        return a

    def add_point(self):
        self.num += 1

    def point_to_a(self, point):
        return point.x * self.m + point.y


class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        adjencents = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        matrix = [[0 for _ in range(m)] for __ in range(n)]
        union = UnionFind(n, m)
        results = []
        for op in operators:
            if matrix[op.x][op.y] == 1:
                results.append(union.num)
                continue

            matrix[op.x][op.y] = 1
            union.add_point()

            for adj in adjencents:
                x_ = op.x + adj[0]
                y_ = op.y + adj[1]
                if x_ < 0 or x_ >= n or y_ < 0 or y_ >= m:
                    continue

                if matrix[x_][y_] == 0:
                    continue

                union.connect(op, Point(x_, y_))

            results.append(union.num)

        return results