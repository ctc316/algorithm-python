"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param coordinates: The radars' coordinate
    @param radius: Detection radius of radars
    @return: The car was detected or not
    """
    def radarDetection(self, coordinates, radius):
        if len(coordinates) == 0:
            return "NO"

        for i in range(len(coordinates)):
            if abs(coordinates[i].y) <= radius[i] and abs(coordinates[i].y - 1) <= radius[i]:
                return "YES"

        return "NO"