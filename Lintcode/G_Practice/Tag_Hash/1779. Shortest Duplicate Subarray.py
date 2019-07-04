class Solution:
    """
    @param arr: The array you should find shortest subarray length which has duplicate elements.
    @return: Return the shortest subarray length which has duplicate elements.
    """
    def getLength(self, arr):
        if not arr or len(arr) < 2:
            return -1

        last_pos = {}
        shortest = 10e6
        for i, num in enumerate(arr):
            if num not in last_pos:
                last_pos[num] = i
            else:
                if i - last_pos[num] < shortest:
                    shortest = i - last_pos[num]
                last_pos[num] = i

        if shortest == 10e6:
            return -1
        return shortest + 1


class Solution:
    """
    @param arr: The array you should find shortest subarray length which has duplicate elements.
    @return: Return the shortest subarray length which has duplicate elements.
    """
    def getLength(self, arr):
        if not arr or len(arr) < 2:
            return -1

        n = len(arr)
        i, j = 0, 0
        last_pos = {}
        shortest = float("Inf")
        while i < n:
            while j < n and arr[j] not in last_pos:
                last_pos[arr[j]] = j
                j += 1

            if j == n or arr[j] not in last_pos:
                break

            dupl_idx = last_pos[arr[j]]
            last_pos[arr[j]] = j
            j += 1

            if j - dupl_idx < shortest:
                shortest = j - dupl_idx

            while i < dupl_idx:
                del last_pos[arr[i]]
                i += 1
            i += 1

        if shortest == float("Inf"):
            return -1
        return shortest