class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        '''
        [0,-2,0,-3,-4,0,0,0]

        -0,-0
        -3 -2

        balance:
        -3,-0
        -0,-2

        '''
        from queue import PriorityQueue
        l_pq = PriorityQueue()  # maxheap
        r_pq = PriorityQueue()  # minheap
        res = []
        for num in nums:
            if l_pq.qsize() <= r_pq.qsize():
                l_pq.put(-num)
            else:
                r_pq.put(num)

            if not l_pq.empty() and not r_pq.empty() and -l_pq.queue[0] > r_pq.queue[0]:
                l = l_pq.get()
                r = r_pq.get()
                l_pq.put(-r)
                r_pq.put(-l)

            res.append(-l_pq.queue[0])

        return res