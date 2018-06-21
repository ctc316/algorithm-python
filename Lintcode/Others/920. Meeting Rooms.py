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
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x: x.start)
        end = 0
        for intv in intervals:
            if intv.start < end:
                return False
                
            if intv.end > end:
                end = intv.end
            
        return True