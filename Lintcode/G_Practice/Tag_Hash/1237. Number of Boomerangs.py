class Solution:
    """
    @param points: a 2D array
    @return: the number of boomerangs
    """
    def numberOfBoomerangs(self, points):
        n = len(points)
        res = 0
        for i in range(n):
            dist_count = {}
            for j in range(n):
                if i == j:
                    continue
                d = self.getDistance(points[i], points[j])
                dist_count[d] = dist_count[d] + 1 if d in dist_count else 1

            for v in dist_count.values():
                res += v * (v - 1)

        return res


    def getDistance(self, p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2