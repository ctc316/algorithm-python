class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.k = k
        from queue import PriorityQueue
        self.pq = PriorityQueue()

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        self.pq.put(num)
        if self.pq.qsize() > self.k:
            self.pq.get()
        
        
    """
    @return: Top k element
    """
    def topk(self):
        return sorted(self.pq.queue)[::-1]