class GraphNode:
    def __init__(self, city):
        self.city = city
        self.adjacents = []  # (city no, price)


class Solution:
    """
    @param n: a integer
    @param flights: a 2D array
    @param src: a integer
    @param dst: a integer
    @param K: a integer
    @return: return a integer
    """
    def findCheapestPrice(self, n, flights, src, dst, K):
        # init nodes
        graph = {}
        for f in flights:
            if f[0] not in graph:
                graph[f[0]] = GraphNode(f[0])
            if f[1] not in graph:
                graph[f[1]] = GraphNode(f[1])

        # init edges
        for f in flights:
            graph[f[0]].adjacents.append((f[1], f[2]))

        from queue import PriorityQueue
        pq = PriorityQueue()
        pq.put((0, src, -1)) # cost, city, stops
        visited = set()
        while not pq.empty():
            cost, city, stops = pq.get()
            visited.add(city)
            if city == dst:
                return cost
            if stops >= K:
                continue
            for adj_city, adj_cost in graph[city].adjacents:
                if adj_city in visited:
                    continue
                pq.put((cost + adj_cost, adj_city, stops + 1))

        return -1