class GraphNode:
    def __init__(self, val):
        self.val = val
        self.adjacents = set()


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        if n == 0 or len(edges) > n - 1:
            return False

        nodeMap = {i:GraphNode(i) for i in range(n)}
        for e in edges:
            nodeMap[e[0]].adjacents.add(nodeMap[e[1]])
            nodeMap[e[1]].adjacents.add(nodeMap[e[0]])

        self.count = 0
        self.dfs(nodeMap[0], set())
        return self.count == n


    def dfs(self, node, visits):
        self.count += 1
        visits.add(node)
        for adj in node.adjacents:
            if adj not in visits:
                self.dfs(adj, visits)
