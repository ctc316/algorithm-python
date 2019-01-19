class Solution:
    """
    @param list: the information of studnet
    @param k:
    @return: return a list
    """
    def topKgpa(self, list, k):
        n = len(list)
        if k >= n:
            return list

        from queue import PriorityQueue
        pq = PriorityQueue()
        for i, l in enumerate(list):
            pq.put((l[1], i))
            if pq.qsize() > k:
                pq.get()

        return [list[i] for i in sorted([pq.get()[1] for _ in range(k)])]