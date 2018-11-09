class Solution:
    """
    @param arrs: an array of arrays
    @return: return the max distance among arrays
    """
    def maxDiff(self, arrs):
        from queue import PriorityQueue
        minq = PriorityQueue()
        maxq = PriorityQueue()
        for i, arr in enumerate(arrs):
            minq.put((arr[0], i))
            maxq.put((-arr[-1], i))

        top_min = minq.get()
        top_max = maxq.get()

        if top_min[1] != top_max[1]:
            return -top_max[0] - top_min[0]

        sec_min = minq.get()
        sec_max = maxq.get()

        return max(-top_max[0] - sec_min[0], top_min[0] - sec_max[0])
