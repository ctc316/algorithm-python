class MyCalendarThree:

    def __init__(self):
        self.calendar = []
        self.largest = 0

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        import bisect
        bisect.insort(self.calendar, (start, 1))
        bisect.insort(self.calendar, (end, -1))
        booked = 0
        startIdx = bisect.bisect_left(self.calendar, (start, 1))
        endIdx = bisect.bisect_left(self.calendar, (end, 1))
        for i in range(0, endIdx):
            if self.calendar[i][0] >= end:
                break
            booked += self.calendar[i][1]
            self.largest = max(self.largest, booked)

        return self.largest


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)