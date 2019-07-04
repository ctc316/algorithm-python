class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        i = j = len(A) - 1
        while i >= 0:
            if A[i] == elem:
                A[i], A[j] = A[j], A[i]
                j -= 1
            i -= 1
        return j + 1