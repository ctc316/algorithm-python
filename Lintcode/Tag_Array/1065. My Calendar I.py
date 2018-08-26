class Intv:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        if self.start == other.start:
            return self.end < other.end
        return self.start < other.start


from bisect import bisect_left

class MyCalendar:

    def __init__(self):
        self.arr = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        '''
        (10, 20), (15, 25), (20, 30)
        '''

        intv = Intv(start, end)
        i = bisect_left(self.arr, intv)
        if (i - 1 < 0 or intv.start >= self.arr[i - 1].end) and \
           (i >= len(self.arr) or intv.end <= self.arr[i].start):
                self.arr.insert(i, intv)
                return True
        return False




# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)