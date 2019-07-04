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
        pos = self.intvBisect(intervals, newInterval)
        intervals.insert(pos, newInterval)

        merge_s = pos
        while merge_s - 1 >= 0 and intervals[merge_s - 1].end >= newInterval.start:
            merge_s -= 1
            newInterval.start = min(newInterval.start, intervals[merge_s].start)
            newInterval.end = max(newInterval.end, intervals[merge_s].end)

        merge_e = pos
        while merge_e + 1 < len(intervals) and intervals[merge_e + 1].start <= newInterval.end:
            merge_e += 1
            newInterval.start = min(newInterval.start, intervals[merge_e].start)
            newInterval.end = max(newInterval.end, intervals[merge_e].end)

        return [intervals[i] for i in range(len(intervals)) if i == pos or i < merge_s or i > merge_e]


    def intvBisect(self, intervals, target):
        if len(intervals) == 0:
            return 0

        l = 0
        r = len(intervals) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if target.start <= intervals[mid].start:
                r = mid
            else:
                l = mid

        if target.start > intervals[r].start:
            return r + 1
        elif target.start > intervals[l].start:
            return r
        else:
            return l