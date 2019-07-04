class Solution:
    """
    @param N: an integer
    @param edges: the edges
    @return: a list ans, where ans[i] is the sum of the distances between node i and all other nodes
    """
    def sumOfDistancesInTree(self, N, edges):
        distances = [0] * N
        subtree_nodes = [1] * N
        neighbors = [[] for _ in range(N)]
        for e in edges:
            neighbors[e[0]].append(e[1])
            neighbors[e[1]].append(e[0])
            
        def dfsCountNodeDistance(parent, node):
            for nei in neighbors[node]:
                if nei == parent:
                    continue
                dfsCountNodeDistance(node, nei)
                subtree_nodes[node] += subtree_nodes[nei]
                distances[node] += distances[nei] + subtree_nodes[nei]
                
        def dfsFinalize(parent, node):
            if parent != -1:
                distances[node] = distances[parent] - subtree_nodes[node] + N - subtree_nodes[node]
            for nei in neighbors[node]:
                if nei == parent:
                    continue
                dfsFinalize(node, nei)
                
        dfsCountNodeDistance(-1, 0)
        dfsFinalize(-1, 0)
        return distances