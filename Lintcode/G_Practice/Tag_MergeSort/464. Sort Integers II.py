class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        self.mergeSort(A, 0, len(A) - 1, [0] * len(A))

    def mergeSort(self, A, start, end, temp):
        if start >= end:
            return

        mid = start + (end - start) // 2
        self.mergeSort(A, start, mid, temp)
        self.mergeSort(A, mid + 1, end, temp)
        self.merge(A, start, mid, end, temp)


    def merge(self, A, start, mid, end, temp):
        left = start
        right = mid + 1
        idx = start
        while left <= mid and right <= end:
            if A[left] < A[right]:
                temp[idx] = A[left]
                left += 1
            else:
                temp[idx] = A[right]
                right += 1
            idx += 1

        while left <= mid:
            temp[idx] = A[left]
            left += 1
            idx += 1

        while right <= end:
            temp[idx] = A[right]
            right += 1
            idx += 1

        for i in range(start, end + 1):
            A[i] = temp[i]