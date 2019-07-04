class Solution:
    """
    @param graph: a 2D integers array
    @return: return a list of integers
    """
    def eventualSafeNodes(self, graph):
        res = set()
        for i in range(len(graph)):
            visited = set([i])
            self.dfs(graph, i, visited, res)
        return sorted(res)


    def dfs(self, graph, i, visited, result):
        for node in graph[i]:
            if node in visited:
                return False
            if node in result:
                continue

            visited.add(node)
            if not self.dfs(graph, node, visited, result):
                return False
            visited.remove(node)

        result.add(i)
        return True
