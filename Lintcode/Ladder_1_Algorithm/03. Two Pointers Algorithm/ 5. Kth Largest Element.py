class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        if len(A) == 0:
            return 0

        return self.quickSelect(A, 0, len(A) - 1, k)


    def quickSelect(self, A, start, end, k):

        pivot = A[start]

        left, right = start, end
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1

            while left <= right and A[right] > pivot:
                right -= 1

            if left <= right:
                tmp = A[left]
                A[left] = A[right]
                A[right] = tmp
                left += 1
                right -= 1

        '''
            1 2 3 4 5
            s r   l e

            k = 2 -> 45
            k = 3 -> 3
            k = 4 -> 12
        '''

        pos_k = end - k + 1
        if pos_k >= left:
            return self.quickSelect(A, left, end, k)
        if pos_k <= right:
            return self.quickSelect(A, start, right, k - (end - right))

        return A[right + 1]  # or A[left - 1]