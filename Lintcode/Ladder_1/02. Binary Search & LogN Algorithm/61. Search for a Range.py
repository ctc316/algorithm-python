#Version 1: find two bound seperately
class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        if A is None or len(A) == 0:
            return [-1, -1]

        # find left bound
        left = -1
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if target <= A[mid]:
                end = mid
            else:
                start = mid

        if A[start] == target:
            left = start
        elif A[end] == target:
            left = end
        else:
            return [-1, -1]

        # find right bound
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if target < A[mid]:
                end = mid
            else:
                start = mid

        if A[end] == target:
            return [left, end]
        return [left, start]
