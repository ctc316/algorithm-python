class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        if A is None or len(A) == 0:
            return 0

        left = 0
        right = len(A) - 1
        while left < right - 1:
            mid = int(left + (right - left) / 2)
            if A[mid] < target:
                left = mid
            else:
                right = mid

        count = 0

        while left > -1 and A[left] == target:
            count += 1
            left -= 1

        while right < len(A) and A[right] == target:
            count += 1
            right += 1

        return count