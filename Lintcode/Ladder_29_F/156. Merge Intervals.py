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
        n = len(intervals)
        if n == 0:
            return []

        intervals.sort(key=lambda x: (x.start, x.end))
        result = []

        cur = intervals[0]
        for i in range(1, n):
            this = intervals[i]
            if this.start <= cur.end:
                cur.end = max(cur.end, this.end)
            else:
                result.append(cur)
                cur = this

        result.append(cur)
        return result