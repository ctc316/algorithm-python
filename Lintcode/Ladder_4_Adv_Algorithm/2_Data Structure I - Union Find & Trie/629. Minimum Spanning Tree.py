'''
Definition for a Connection
class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost
'''
class Solution:
    # @param {Connection[]} connections given a list of connections
    # include two cities and cost
    # @return {Connection[]} a list of connections from results
    def lowestCost(self, connections):
        connections.sort(key=lambda x: (x.cost, x.city1, x.city2))
        self.father = {}
        self.count = 0

        # init graph and fathers
        for conn in connections:
            if conn.city1 not in self.father:
                self.father[conn.city1] = conn.city1
                self.count += 1

            if conn.city2 not in self.father:
                self.father[conn.city2] = conn.city2
                self.count += 1

        # union
        results = []
        for conn in connections:
            root1 = self.find(conn.city1)
            root2 = self.find(conn.city2)
            if root1 != root2:
                self.father[self.find(root1)] = self.find(root2)
                self.count -= 1
                results.append(conn)

        if self.count == 1:
            return results

        return []


    def find(self, node):
        path = []
        while self.father[node] != node:
            path.append(node)
            node = self.father[node]

        for p in path:
            self.father[p] = node

        return node