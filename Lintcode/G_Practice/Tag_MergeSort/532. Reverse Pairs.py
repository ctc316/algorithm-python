class Solution:
    """
    @param A: an array
    @return: total of reverse pairs
    """
    def reversePairs(self, A):
        self.count = 0
        self.mergeSort(A, 0, len(A) - 1, [0] * len(A))
        return self.count

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
            if A[left] <= A[right]:
                temp[idx] = A[left]
                if left > idx:
                    self.count += left - idx
                idx += 1
                left += 1
            else:
                temp[idx] = A[right]
                if right > idx:
                    self.count += right - idx
                idx += 1
                right += 1

        while left <= mid:
            temp[idx] = A[left]
            if left > idx:
                self.count += left - idx
            idx += 1
            left += 1

        while right <= end:
            temp[idx] = A[right]
            if right > idx:
                self.count += right - idx
            idx += 1
            right += 1

        for i in range(start, end + 1):
            A[i] = temp[i]

