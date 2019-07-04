class Solution:
    """
    @param array: a 2D array
    @return: the minimum difference
    """
    def minimumDifference(self, array):
        if not array or len(array) == 0 or len(array[0]) == 0:
            return 0

        n, m = len(array), len(array[0])
        from queue import PriorityQueue
        pq = PriorityQueue()
        for i in range(n):
            pq.put((array[i][0], i, 0))
        max_of_curr = max(pq.queue)[0]
        min_diffs = float("Inf")

        while True:
            val, i, j = pq.get()
            min_diffs = min(min_diffs, max_of_curr - val)
            if j + 1 == m:
                break
            pq.put((array[i][j + 1], i, j + 1))
            max_of_curr = max(max_of_curr, array[i][j + 1])

        return min_diffs





from heapq import heapify, heappush, heappop, heappushpop
class Solution:
    def minimumDifference(self, array):
        n, m = len(array), len(array[0])
        min_heap = [(array[i][0], i, 0) for i in range(n)]
        heapify(min_heap)
        max_of_mins = max(array[i][0] for i in range(n))
        min_diffs = float("Inf")
        
        while True:
            val, i, j = min_heap[0]
            min_diffs = min(min_diffs, max_of_mins - min_heap[0][0])
            if j + 1 == m:
                break
            heappushpop(min_heap, (array[i][j + 1], i, j + 1))
            max_of_mins = max(max_of_mins, array[i][j + 1])
            
        return min_diffs