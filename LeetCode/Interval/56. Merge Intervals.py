class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        intervals.sort()

        i = 0
        while i < len(intervals) - 1:
            this = intervals[i]
            next = intervals[i + 1]
            if this[1] >= next[0]:
                this[1] = max(this[1], next[1])
                del intervals[i + 1]
            else:
                i += 1

        return intervals