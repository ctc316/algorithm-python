"""
Definition for a directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

class UnionFind:
    def __init__(self, nodes):
        self.parent = {}
        for n in nodes:
            self.parent[n] = n


    def find(self, a):
        path = []
        while a != self.parent[a]:
            path.append(a)
            a = self.parent[a]

        for p in path:
            self.parent[p] = a

        return a


    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.parent[root_b] = root_a


class Solution:
    """
    @param: nodes: a array of Directed graph node
    @return: a connected set of a directed graph
    """
    def connectedSet2(self, nodes):
        union = UnionFind(nodes)
        for node in nodes:
            for neigh in node.neighbors:
                union.union(node, neigh)

        from bisect import bisect_left
        groups = {}
        for node in nodes:
            root = union.find(node)
            if root.label not in groups:
                groups[root.label] = []

            idx = bisect_left(groups[root.label], node.label)
            groups[root.label].insert(idx, node.label)


        keys = []
        items = []
        for k, v in groups.items():
            idx = bisect_left(keys, k)
            keys.insert(idx, k)
            items.insert(idx, v)

        return items