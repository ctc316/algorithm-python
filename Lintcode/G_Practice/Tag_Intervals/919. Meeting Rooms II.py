"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        from queue import PriorityQueue
        timeline = PriorityQueue()
        for intv in intervals:
            timeline.put((intv.start, 1))
            timeline.put((intv.end, -1))

        minimum = 0
        rooms = 0
        while not timeline.empty():
            rooms += timeline.get()[1]
            minimum = max(minimum, rooms)

        return minimum