import bisect
class Solution:
    """
    @param a: the first list
    @param b: the second list
    @param x: the max sum
    @return: the pairs whose sum are not exceed x
    """
    def getAns(self, a, b, x):
        a.sort()
        b.sort()
        
        minDelta = sys.maxsize
        pairList = []
        for first in a:
            if first > x:
                break   # all elements and target are non negative, so there is no more matches
            targetSum = x - first
            
            index = bisect.bisect(b, targetSum)
            if index == 0:
                break       # end the loop here since first is getting too large for second to match
            second = b[index-1]
            
            delta = x - first - second
            if delta < minDelta:
                minDelta = delta 
                pairList.clear()
                pairList.append([first, second])
            elif delta == minDelta:
                pairList.append([first, second])
                
        return pairList