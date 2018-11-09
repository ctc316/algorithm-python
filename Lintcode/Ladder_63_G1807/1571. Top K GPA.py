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
        for i in range(n):
            pq.put((-float(list[i][1]), (i, list[i])))


        pq2 = PriorityQueue()
        for _ in range(k):
            pq2.put(pq.get()[1])


        results = []
        while not pq2.empty():
            results.append(pq2.get()[1])

        return results