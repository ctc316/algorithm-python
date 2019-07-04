class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def findRadius(self, houses, heaters):
        heaters.sort()
        res = 0
        for h in houses:
            res = max(res, self.closestHeater(h, heaters))
        return res

    def closestHeater(self, house, heaters):
        start = 0
        end = len(heaters) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if heaters[mid] == house:
                return 0
            elif heaters[mid] < house:
                start = mid
            else:
                end = mid
        return min(abs(house - heaters[start]), abs(heaters[end] - house))