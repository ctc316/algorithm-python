"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
       return sorted(points, key=lambda p: ((p.x - origin.x)**2 + (p.y - origin.y)**2, p.x, p.y))[:k]