class Solution:
    """
    @param points: n points on a 2D plane
    @return: if there is such a line parallel to y-axis that reflect the given points
    """
    def isReflected(self, points):
        pointsByY = {}
        for p in points:
            if p[1] not in pointsByY:
                pointsByY[p[1]] = []
            pointsByY[p[1]].append(p[0])

        reflect = None
        for pair in pointsByY.values():
            pair.sort()
            l = 0
            r = len(pair) - 1
            while l <= r:
                if reflect is None:
                    reflect = (pair[l] + pair[r]) / 2
                elif (pair[l] + pair[r]) / 2 != reflect:
                    return False
                l += 1
                r -= 1

        return True