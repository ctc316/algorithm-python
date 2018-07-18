# Version 1: Priority Queue, Time: O(nlogn)
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        k = len(arrays)
        if k == 0:
            return []

        from queue import PriorityQueue
        pq = PriorityQueue()

        for i in range(k):
            for ele in arrays[i]:
                pq.put(ele)

        results = []
        while pq.qsize():
            results.append(pq.get())

        return results



# Version 2: Priority Queue for Limited Memory, Time: O(nlogn), Memory: O(k), Disk: O(N)
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        k = len(arrays)
        if k == 0:
            return []

        from queue import PriorityQueue
        pq = PriorityQueue()

        # init: put every [0] to pq
        for i in range(k):
            if len(arrays[i]) > 0:
                pq.put((arrays[i][0], arrays[i], 1))  # (value, array pointer, next)

        # every round, pop one min value, and put the next value in the same array in.
        results = []
        while not pq.empty():
            val, arr, next = pq.get()
            results.append(val)
            if next < len(arr):
                pq.put((arr[next], arr, next + 1))

        return results