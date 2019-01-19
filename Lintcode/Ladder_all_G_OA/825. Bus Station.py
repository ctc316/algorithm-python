class Solution:
    """
    @param N: The number of buses
    @param route: The route of buses
    @param A: Start bus station
    @param B: End bus station
    @return: Return the minimum transfer number
    """
    def getMinTransferNumber(self, N, route, A, B):
        # build route map for every station (station: routeIdList)
        route_map = {}
        for i in range(N):
            for station in route[i]:
                if station not in route_map:
                    route_map[station] = set()

                route_map[station].add(i)


        # BFS, start from A
        from queue import Queue
        q = Queue()
        visited_station = set()
        visited_route = set()

        q.put(A)
        visited_station.add(A)

        transfer = 0

        while not q.empty():
            transfer += 1
            for i in range(q.qsize()):
                station = q.get()
                for route_id in route_map[station]:
                    # check every route of the station
                    if route_id in visited_route:
                        continue
                    visited_route.add(route_id)

                    # if this route is in B's route list, then we can reach B
                    if route_id in route_map[B]:
                        return transfer

                    for neighbor in route[route_id]:
                        # check every station we can reach in the route as a transfer station
                        if neighbor in visited_station:
                            continue
                        visited_station.add(neighbor_station)
                        q.put(neighbor_station)

        return -1