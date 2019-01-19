class Solution:
    """
    @param arrayIn: The original array.
    @return: Count the minimum number of subarrays.
    """
    def LeastSubsequences(self, arrayIn):
        cur_mins = []
        for num in arrayIn:
            idx = self.binarySearch(cur_mins, num)
            if idx == len(cur_mins):
                cur_mins.append(num)
            else:
                cur_mins[idx] = num

        return len(cur_mins)


    def binarySearch(self, arr, target):
        if len(arr) == 0:
            return 0

        left = 0
        right = len(arr) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if target < arr[mid]:
                right = mid
            else:
                left = mid

        if target < arr[left]:
            return left
        if target < arr[right]:
            return right
        return right + 1