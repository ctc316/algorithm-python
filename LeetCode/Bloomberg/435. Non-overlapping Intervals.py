class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removes = 0
        end = float("-inf")
        for i in sorted(intervals):
            if i[0] >= end:
                end = i[1]
            else:
                removes += 1 
                end = min(end, i[1])
                
        return removes