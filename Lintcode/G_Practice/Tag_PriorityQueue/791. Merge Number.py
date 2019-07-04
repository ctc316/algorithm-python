class Solution:
    """
    @param numbers: the numbers
    @return: the minimum cost
    """
    def mergeNumber(self, numbers):
        if not numbers or len(numbers) < 2:
            return 0

        from Queue import PriorityQueue
        pq = PriorityQueue()
        for num in numbers:
            pq.put(num)

        total = 0
        while pq.qsize() > 1:
            engy = pq.get() + pq.get()
            total += engy
            pq.put(engy)

        return total