class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.num = n

    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.parent[root_b] = root_a
            self.num -= 1

    def find(self, a):
        path = []
        while self.parent[a] != a:
            path.append(a)
            a = self.parent[a]

        for p in path:
            self.parent[p] = a

        return a


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        if n == 0 or len(edges) != n - 1:
            return False

        union = UnionFind(n)
        for e in edges:
            union.connect(e[0], e[1])

        return union.num == 1