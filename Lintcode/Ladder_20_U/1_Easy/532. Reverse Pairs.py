# Version 1: Merge Sort
class Solution:
    """
    @param A: an array
    @return: total of reverse pairs
    """
    def reversePairs(self, A):
        return self.mergeSort(A, 0, len(A) - 1)


    def mergeSort(self, A, start, end):
        if start >= end:
            return 0

        mid = start + int((end - start) / 2)
        return self.mergeSort(A, start, mid) + \
               self.mergeSort(A, mid + 1, end) + \
               self.merge(A, start, mid, end)


    def merge(self, A, start, mid, end):
        temp = []
        left = start
        right = mid + 1
        count = 0
        while left <= mid and right <= end:
            if A[left] > A[right]:
                temp.append(A[right])
                count += mid - left + 1
                right += 1
            else:
                temp.append(A[left])
                left += 1

        while left <= mid:
            temp.append(A[left])
            left += 1

        while right <= end:
            temp.append(A[right])
            right += 1

        # replace values in the orig arr
        for i in range(start, end + 1):
            A[i] = temp[i - start]

        return count