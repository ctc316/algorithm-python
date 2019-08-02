"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param a: the array a
    @return: return the minimal points number
    """
    def getAns(self, a):
        if not a:
            return 0
            
        a.sort(key=lambda x: (x.start, x.end))
        start = a[0].start
        end = a[0].end
        count = 1
        for i in range(1, len(a)):
            if a[i].start <= end:
                end = min(end, a[i].end)
            else:
                end = a[i].end
                count += 1
    
        return count