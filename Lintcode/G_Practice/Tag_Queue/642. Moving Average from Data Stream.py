class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        self.summ = 0
        self.size = size
        from queue import Queue
        self.q = Queue()

    """
    @param: val: An integer
    @return:
    """
    def next(self, val):
        self.q.put(val)
        self.summ += val
        if self.q.qsize() > self.size:
            self.summ -= self.q.get()
            return self.summ / self.size
        return self.summ / self.q.qsize()


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)