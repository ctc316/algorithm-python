# Version 1: Binary Search, Time: O(nlogn)
class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        n = len(A)
        if n == 0:
            return 0
            
        '''
            Prefix[j] - Prefix[i] 必须在A和B之间，
            公式转换为 A + Prefix[i] < Prefix[j] < B + Prefix[i]，
            原数组因为是全部Positive，所以PrefixSum复合递增的规律，
            可以用BinarySearch找到j的范围，使其满足上面的等式。
        '''
        
        prefixSum = [0 for _ in range(n + 1)]
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + A[i]
        
        '''
            for each prefixSum, find range(i, j1) < leftbound, 
                                     range(i, j2) < rightbound + 1,
            ans += j2 - j1
        '''
        count = 0
        for i in range(1, n + 1):
            if prefixSum[i] >= start and prefixSum[i] <= end:
                count += 1
            count += self.findBound(prefixSum, i, end + 1) - self.findBound(prefixSum, i, start) 
        
        return count
    
    
    def findBound(self, prefixSum, startIdx, bound):
        left = startIdx
        right = len(prefixSum) - 1
        bound += prefixSum[startIdx]
        
        while left + 1 < right:
            mid = int(left + (right - left) / 2)
            if prefixSum[mid] >= bound:
                right = mid 
            else:
                left = mid
                
        if prefixSum[right] >= bound:
            return left
        return right



# Version 2: prefix sum + two pointer,  Time: O(n^2), TLE
class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        n = len(A)
        if n == 0:
            return 0

        prefixSum = [0 for _ in range(n + 1)]
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + A[i]

        count = 0
        for left in range(n):
            for right in range(left, n):
                subsum = prefixSum[right + 1] - prefixSum[left]
                if subsum >= start and subsum <= end:
                    count += 1

        return count