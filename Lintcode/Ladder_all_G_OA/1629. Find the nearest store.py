class Solution:
    """
    @param stores: The location of each store.
    @param houses: The location of each house.
    @return: The location of the nearest store to each house.
    """
    def findNearestStore(self, stores, houses):
        from bisect import bisect_left
        stores = sorted(stores)
        result = []
        for house in houses:
            pos = bisect_left(stores, house)
            if pos == 0:
                result.append(stores[0])
            elif pos == len(stores):
                result.append(stores[-1])
            elif house - stores[pos - 1] <= stores[pos] - house:
                result.append(stores[pos - 1])
            else:
                result.append(stores[pos])

        return result