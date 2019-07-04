class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        from bisect import bisect_left
        r = bisect_left(A, target)
        l = r - 1
        res = []
        for _ in range(k):
            if l < 0:
                res.append(A[r])
                r += 1
            elif r == len(A) or abs(A[l] - target) <= abs(A[r] - target):
                res.append(A[l])
                l -= 1
            else :
                res.append(A[r])
                r += 1

        return res