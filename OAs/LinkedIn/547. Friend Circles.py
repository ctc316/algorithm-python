class UnionFind:
    def __init__(self, m):
        self.m = m
        self.parent = [i for i in range(m)]
        self.count = m

    def find(self, i):
        path = []
        while i != self.parent[i]:
            path.append(i)
            i = self.parent[i]

        for p in path:
            self.parent[p] = i

        return i


    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parent[root_a] = root_b
            self.count -= 1


class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        union = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j]:
                    union.connect(i, j)

        return union.count