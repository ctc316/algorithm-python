class MyCalendarTwo:

    def __init__(self):
        from queue import PriorityQueue
        self.timeline = PriorityQueue()

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """

        snapshot = [item for item in self.timeline.queue]
        self.timeline.put((start, 1))
        self.timeline.put((end, -1))
        counts = 0
        available = True
        while not self.timeline.empty():
            time, action = self.timeline.get()
            counts += action
            if counts > 2:
                available = False
                break

            if time > end:
                break

        self.timeline.queue = snapshot
        if available:
            self.timeline.put((start, 1))
            self.timeline.put((end, -1))
            return True
        else:
            return False



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)