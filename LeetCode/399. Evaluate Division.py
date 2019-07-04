class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = {}  #{node: {neighbor: value}}
        for i, e in enumerate(equations):
            if e[0] not in edges:
                edges[e[0]] = {}
            edges[e[0]][e[1]] = values[i]
            if e[1] not in edges:
                edges[e[1]] = {}
            edges[e[1]][e[0]] = 1 / values[i]

        return [self.findPathValue(edges, q[0], q[1]) for q in queries]


    def findPathValue(self, edges, start, end):
        if start not in edges:
            return -1.0

        from queue import Queue
        q = Queue()
        visited = set()
        q.put((start, 1))
        visited.add(start)

        while not q.empty():
            node, val = q.get()
            if node == end:
                return val

            for nei, edge_val in edges[node].items():
                if nei in visited:
                    continue

                visited.add(nei)
                q.put((nei, val * edge_val))

        return -1.0
