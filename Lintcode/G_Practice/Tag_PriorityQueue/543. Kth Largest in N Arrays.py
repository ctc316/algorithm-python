class Solution:
    """
    @param arrays: a list of array
    @param k: An integer
    @return: an integer, K-th largest element in N arrays
    """
    def KthInArrays(self, arrays, k):
        from queue import PriorityQueue
        pq = PriorityQueue()
        for row in arrays:
            for val in row:
                if pq.qsize() >= k:
                    if val <= pq.queue[0]:
                        continue
                    pq.get()
                pq.put(val)
        return pq.get()