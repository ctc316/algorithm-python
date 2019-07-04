'''
Give two users' ordered online time series, and each section records
the user's login time point x and offline time point y. Find out the
time periods when both users are online at the same time, and output
in ascending order.

We guarantee that the length of online time series meet 1 <= len <= 1e6.
For a user's online time series, any two of its sections do not intersect.
Have you met this question in a real interview?

Example
Example 1:

Input: seqA = [(1,2),(5,100)], seqB = [(1,6)]
Output: [(1,2),(5,6)]
Explanation: In these two time periods (1,2), (5,6), both users are online at the same time.
Example 2:

Input: seqA = [(1,2),(10,15)], seqB = [(3,5),(7,9)]
Output: []
Explanation: There is no time period, both users are online at the same time.
Related Problems

'''


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param seqA: the list of intervals
    @param seqB: the list of intervals
    @return: the time periods
    """
    def timeIntersection(self, seqA, seqB):
        from queue import PriorityQueue
        timeline = PriorityQueue()
        for seq in seqA:
            timeline.put((seq.start, 1))
            timeline.put((seq.end, -1))
        for seq in seqB:
            timeline.put((seq.start, 1))
            timeline.put((seq.end, -1))

        start = -1
        pre_users = 0
        users = 0
        res = []
        while not timeline.empty():
            time, diff = timeline.get()
            pre_users = users
            users += diff
            if start == -1 and pre_users == 1 and users == 2:
                start = time
            elif pre_users == 2 and users == 1:
                res.append(Interval(start, time))
                start = -1

        return res