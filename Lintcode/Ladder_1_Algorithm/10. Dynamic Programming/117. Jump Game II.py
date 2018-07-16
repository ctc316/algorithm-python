# Version 1: DP,  O(n^2), TLE
class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        n = len(A)
        if n == 0:
            return 0
            
        jumps = [sys.maxsize for _ in range(n)]
        jumps[0] = 0
        
        for i in range(1, n):
            for j in range(i, -1, -1):
                if jumps[j] == sys.maxsize or j + A[j] < i:
                    continue
                
                jumps[i] = min(jumps[i], jumps[j] + 1)
                
        return jumps[n - 1]



# Version 2: Greedy (Level Order), 
class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        n = len(A)
        if n == 0:
            return 0
            
        start = end = jumps = 0
        while end < n - 1:
            jumps += 1
            farthest = end
            for i in range(start, end + 1):
                farthest = max(farthest, A[i] + i)
            
            start = end + 1
            end = farthest
            
        return jumps