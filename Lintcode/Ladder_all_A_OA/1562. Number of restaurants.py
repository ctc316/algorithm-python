class Solution:
    """
    @param restaurant:
    @param n:
    @return: nothing
    """
    def nearestRestaurant(self, restaurant, n):
        if n == 0 or n > len(restaurant):
            return []

        entrys = [(x * x + y * y, (x,y)) for i, (x, y) in enumerate(restaurant)]
        dist_bound = sorted(entrys)[n - 1][0]
        return [point for distance, point in entrys if distance <= dist_bound]