# Version 1: Hash Map, Time: O(n)
class Solution:
    """
    @param nums: the arrays
    @param k: the distance of the same number
    @return: the ans of this question
    """
    def sameNumber(self, nums, k):
        if len(nums) < 2:
            return "NO"
            
        records = {}
        for i in range(len(nums)):
            val = nums[i]
            if val in records and i - records[val] < k:
                    return "YES"
            
            records[val] = i
            
        return "NO"


# Version 2: Sorting by priorty queue, Time: O(nlogn)
class PQEntry:
    def __init__(self, num, idx):
        self.num = num
        self.idx = idx

    def __lt__(self, other):
        if self.num == other.num:
            return self.idx < other.idx
        return self.num < other.num


class Solution:
    """
    @param nums: the arrays
    @param k: the distance of the same number
    @return: the ans of this question
    """
    def sameNumber(self, nums, k):
        if len(nums) < 2:
            return "NO"

        from queue import PriorityQueue
        pq = PriorityQueue()

        for i in range(len(nums)):
            pq.put(PQEntry(nums[i], i))

        prev = pq.get()
        while not pq.empty():
            curr = pq.get()
            if curr.num == prev.num:
                if curr.idx - prev.idx < k:
                    return "YES"
            else:
                prev = curr

        return "NO"