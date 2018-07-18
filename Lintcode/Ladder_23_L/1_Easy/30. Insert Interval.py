"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        intervals.insert(0, newInterval)

        i = 0
        while i < len(intervals) - 1:
            if intervals[i].end < intervals[i + 1].start:
                break

            if intervals[i].start > intervals[i + 1].end:
                self.swap(intervals, i, i + 1)
                i += 1
                continue

            intervals[i] = self.merge(intervals[i], intervals[i + 1])
            intervals.pop(i + 1)

        return intervals


    def merge(self, a, b):
        return Interval(min(a.start, b.start), max(a.end, b.end))

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp