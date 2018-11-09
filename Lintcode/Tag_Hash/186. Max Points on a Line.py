"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param points: an array of point
    @return: An integer
    """
    def maxPoints(self, points):
        n = len(points)
        if n < 3:
            return n

        maxi = 0
        for i in range(n):
            # shared point changed, map should be cleared and server the new point
            # slope_intercept: counts, maybe all points contained in the list are same points, and same points' k is represented by Integer.MIN_VALUE
            slopes = {-sys.maxsize - 1: 1}
            duplicate = 0
            for j in range(i + 1, n):
                if points[i].x == points[j].x:
                    if points[i].y == points[j].y:
                        duplicate += 1
                        continue

                    slope = sys.maxsize
                else:
                    slope = (points[i].y - points[j].y) / (points[i].x - points[j].x)

                if slope not in slopes:
                    slopes[slope] = 2
                else:
                    slopes[slope] += 1


            for val in slopes.values():
                maxi = max(maxi, val + duplicate)

        return maxi