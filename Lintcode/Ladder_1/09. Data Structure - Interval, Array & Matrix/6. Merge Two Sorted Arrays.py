# Version 1: merge, Time: O(n+m)
class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        n = len(A)
        m = len(B)
        p1 = p2 = 0
        results = []
        while p1 < n and p2 < m:
            if A[p1] < B[p2]:
                results.append(A[p1])
                p1 += 1
            else:
                results.append(B[p2])
                p2 += 1

        if p1 < n:
            results.extend(A[p1:n])

        if p2 < m:
            results.extend(B[p2:m])

        return results



# Version 2: Binary search and insert, Time: O(mlogn), should be faster if n >>> m
class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # make B the smaller one
        if len(A) < len(B):
            temp = A
            A = B
            B = temp

        # binary search and insert
        for ele in B:
            left = 0
            right = len(A) - 1
            while left + 1 < right:
                mid = int(left + (right - left) / 2)
                if ele < A[mid]:
                    right = mid
                else:
                    left = mid

            if ele < A[left]:
                A.insert(left, ele)
            elif ele > A[right]:
                A.insert(right + 1, ele)
            else:
                A.insert(right, ele)

        return A