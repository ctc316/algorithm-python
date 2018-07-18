"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        if len(intervals) == 0:
            return []

        intervals.sort(key=lambda x: (x.start, x.end))
        results = []

        start = intervals[0].start
        end = intervals[0].end
        intervals.pop(0)

        for intv in intervals:
            if intv.start > end:
                results.append(Interval(start, end))
                start = intv.start
                end = intv.end
            elif intv.end > end:
                end = intv.end

        results.append(Interval(start, end))

        return results