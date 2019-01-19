class Solution:
    """
    @param a: array a
    @param b: the query array
    @return: Output an array of length `b.length` to represent the answer
    """
    def minimalDistance(self, a, b):
        a.sort()
        result = []
        for target in b:
            closest = self.binarySearch(a, target)
            if len(closest) > 1 and abs(target - closest[0]) > abs(target - closest[1]):
                result.append(closest[1])
            else:
                result.append(closest[0])

        return result


    def binarySearch(self, arr, num):
        if len(arr) < 2:
            return arr

        left = 0
        right = len(arr) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if arr[mid] < num:
                left = mid
            else:
                right = mid

        return [arr[left], arr[right]]



class Solution:
    """
    @param a: array a
    @param b: the query array
    @return: Output an array of length `b.length` to represent the answer
    """
    def minimalDistance(self, a, b):
        from bisect import bisect_left
        a = sorted(a)
        result = []
        for target in b:
            pos = bisect_left(a, target)
            if pos == 0:
                result.append(a[0])
            elif pos == len(a):
                result.append(a[-1])
            elif target - a[pos - 1] <= a[pos] - target:
                result.append(a[pos - 1])
            else:
                result.append(a[pos])

        return result