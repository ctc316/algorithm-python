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
        if not intervals:
            return []

        intervals.sort(key=lambda x: (x.start, x.end))
        result = []
        cur = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i].start <= cur.end:
                cur.end = max(cur.end, intervals[i].end)
            else:
                result.append(cur)
                cur = intervals[i]

        result.append(cur)
        return result