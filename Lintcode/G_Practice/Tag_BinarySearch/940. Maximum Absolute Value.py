class Solution:
    """
    @param A: an array
    @param n: an integer
    @return: makes the smallest absolute value of the difference between any two elements to largest
    """
    def maximumAbsolutValue(self, A, n):
        A.sort()
        l = 0
        r = A[len(A) - 1] - A[0]
        while l + 1 < r:
            mid = l + (r - l) // 2
            if self.checkAbsValue(A, mid) >= n:
                l = mid
            else:
                r = mid

        if self.checkAbsValue(A, r) >= n:
            return r
        return l


    def checkAbsValue(self, A, absVal):
        i = 0
        j = 1
        num = 1
        while j < len(A):
            if A[j] - A[i] >= absVal:
                i = j
                num += 1
            j += 1
        return num