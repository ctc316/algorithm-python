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
        if self.pq.qsize() == self.k:
            if num < self.pq.queue[0]:
                return
            self.pq.get()
        self.pq.put(num)
            
        
    """
    @return: Top k element
    """
    def topk(self):
        return sorted(self.pq.queue, reverse=True)