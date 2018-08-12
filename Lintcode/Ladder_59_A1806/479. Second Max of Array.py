class Solution:
    """
    @param nums: An integer array
    @return: The second max number in the array.
    """
    def secondMax(self, nums):
        from queue import PriorityQueue
        pq = PriorityQueue()
        
        for num in nums:
            pq.put(num)
            if pq.qsize() > 2:
                pq.get()
        
        return pq.queue[0]