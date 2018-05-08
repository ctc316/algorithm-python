# Binary Search, Time: O(nlogm)
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        if len(L) == 0:
            return 0
            
        start = 0
        end = 1e10
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if self.cutByLength(L, mid) < k:
                end = mid
            else:
                start = mid
        
        if self.cutByLength(L, end) >= k:
            return end
        
        return start
            

    def cutByLength(self, L, length):
        pieces = 0
        for l in L:
            pieces += int(l / length)
        
        return pieces