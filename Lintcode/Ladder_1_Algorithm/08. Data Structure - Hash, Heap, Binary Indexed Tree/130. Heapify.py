# Version 1: heap sort, Time: O(nlogn)
class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
        def heapify(self, A):
        for i in range(1, len(A)):
            while i > 0:
                parent = int((i - 1) / 2)
                if parent < 0 or A[i] >= A[parent]:
                    break

                self.swap(A, i, parent)
                i = parent


    def swap(self, A, a, b):
        temp = A[a]
        A[a] = A[b]
        A[b] = temp



# Version 2: sift down, Time: O(n)
class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        for i in range(int(len(A) / 2), -1, -1):
            self.siftdown(A, i)

    def siftdown(self, A, pos):
        while pos < len(A):
            smallest = pos

            left = pos * 2 + 1
            if left < len(A) and A[left] < A[smallest]:
                smallest = left

            right = pos * 2 + 2
            if right < len(A) and A[right] < A[smallest]:
                smallest = right

            if pos == smallest:
                break

            # swap
            A[smallest], A[pos] = A[pos], A[smallest]
            pos = smallest