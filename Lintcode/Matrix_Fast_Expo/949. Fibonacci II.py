# Binary Search + Memorization + mod 10000 (題目要求), Time: O(logn)
class Solution:
    """
    @param n: an integer
    @return: return a string
    """
    def lastFourDigitsOfFn(self, n):
        result = [[1, 1], [1, 0]]
        records = {}
        while n > 0:
            times = 1
            base = [[1, 1], [1, 0]]
            while times * 2 < n:
                times *= 2
                if times in records:
                    base = records[times]
                else:
                    base = self.multiplyMatrix(base, base)
                    records[times] = base
            
            n -= times
            result = self.multiplyMatrix(base, result)
            
        if result[1][1] == 0:
            return str(0)
            
        return str(result[1][1]).zfill(4)
                
    
    def multiplyMatrix(self, A ,B):
        result = [[0 for _ in range(2)] for __ in range(2)]
        for row in range(2):
            for col in range(2):
                for k in range(2):
                    result[row][col] += A[row][k] * B[k][col] 
                    result[row][col] %= 10000
        return result