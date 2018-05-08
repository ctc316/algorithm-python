# Version 1: Brute Force, Time: O(n)
class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean
    """
    def search(self, A, target):
        for i in range(len(A)):
            if A[i] == target:
                return True

        return False



# Version 2: Binary Search, Time: O(n)
class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean
    """
    def search(self, A, target):
        if len(A) == 0:
            return False

        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if A[mid] == A[end]:
                end -= 1
            elif A[mid] >= A[start]:
                if target < A[mid] and target >= A[start]:
                    end = mid
                else:
                    start = mid
            else:
                if target > A[mid] and target <= A[end]:
                    start = mid
                else:
                    end = mid

        if A[start] == target or A[end] == target:
            return True

        return False