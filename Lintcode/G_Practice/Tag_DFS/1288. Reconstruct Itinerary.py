class Solution:
    """
    @param tickets: 
    @return: nothing
    """
    def findItinerary(self, tickets):
        targets = {}
        for a, b in reversed(sorted(tickets)):
            if a in targets:
                targets[a].append(b)
            else:
                targets[a] = [b]
        
        route = []
        self.dfs('JFK', targets, route)
        return route[::-1]
    
    
    def dfs(self, airport, targets, route):
        while airport in targets and targets[airport]:
            self.dfs(targets[airport].pop(), targets, route)
        route.append(airport)



## memory limitation

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.adjacents = set()


class Solution:
    """
    @param tickets:
    @return: nothing
    """
    def findItinerary(self, tickets):
        nodeMap = {}
        for t in tickets:
            if t[0] not in nodeMap:
                nodeMap[t[0]] = GraphNode(t[0])
            if t[1] not in nodeMap:
                nodeMap[t[1]] = GraphNode(t[1])

        for t in tickets:
            nodeMap[t[0]].adjacents.add(nodeMap[t[1]])

        result = []
        self.dfs(nodeMap['JFK'], result)
        return result


    def dfs(self, node, result):
        for adj in node.adjacents:
            result.append(node.val)
            self.dfs(adj, result)

        if not node.adjacents:
            result.append(node.val)
