class Solution:
    """
    @param map: the map
    @return: can you reach the endpoint
    """
    def reachEndpoint(self, map):
        n = len(map)
        if n == 0:
            return False
        m = len(map[0])

        canReach = [[False for _ in range(m + 1)] for __ in range(n + 1)]
        canReach[1][0] = True

        for i in range(n):
            for j in range(m):
                if map[i][j] != 0 and (canReach[i][j + 1] or canReach[i + 1][j]):
                    canReach[i + 1][j + 1] = True

                if map[i][j] == 9:
                    return canReach[i + 1][j + 1]

        return False