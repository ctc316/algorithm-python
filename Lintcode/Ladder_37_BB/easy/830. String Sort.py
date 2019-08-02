class Solution:
    """
    @param str: the string that needs to be sorted
    @return: sorted string
    """
    def stringSort(self, str):
        counts = {}
        for ch in str:
            counts[ch] = counts.get(ch, 0) + 1

        from queue import PriorityQueue
        pq = PriorityQueue()
        for ch in str:
            pq.put((-counts[ch], ch))

        res = ""
        while not pq.empty():
            res += pq.get()[1]

        return res