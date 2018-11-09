class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        start = 0
        end = len(A) - 1
        while start < end:
            while start < end and A[start] % 2 == 0:
                start += 1
            while start < end and A[end] % 2 != 0:
                end -= 1

            if A[start] % 2 != 0:
                temp = A[start]
                A[start] = A[end]
                A[end] = temp

            start += 1
            end -= 1

        return A