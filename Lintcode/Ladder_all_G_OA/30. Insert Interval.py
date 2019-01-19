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
        result = []
        pos = 0
        for intv in intervals:
            if intv.end < newInterval.start:
                result.append(intv)
                pos += 1

            elif intv.start > newInterval.end:
                result.append(intv)

            else:
                newInterval.start = min(intv.start, newInterval.start)
                newInterval.end = max(intv.end, newInterval.end)

        result.insert(pos, newInterval)
        return result