class Solution:
    """
    @param arr: the arr
    @return: the length of the longset subarray
    """
    def pickFruits(self, arr):
        n = len(arr)
        records = {}
        maximum = 0
        j = 0
        for i in range(n):
            while j < n and (len(records) < 2 or len(records) == 2 and arr[j] in records):
                records[arr[j]] = records.get(arr[j], 0) + 1
                j += 1

            maximum = max(maximum, j - i)

            if arr[i] in records:
                records[arr[i]] -= 1
                if records[arr[i]] == 0:
                    del records[arr[i]]

        return maximum