from queue import Queue
from collections import deque

class MaxQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.que = Queue()
        self.max_deque = deque()


    def put(self, val):
        if self.que.qsize() >= self.capacity:
            self.pop()

        self.que.put(val)
        while len(self.max_deque) > 0 and val > self.max_deque[-1]:
            self.max_deque.pop()
        self.max_deque.append(val)


    def pop(self):
        val = self.que.get()
        if val == self.max_deque[0]:
            self.max_deque.popleft()


    def getMax(self):
        return self.max_deque[0]


class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        if k == 0 or len(nums) < k:
            return []

        mq = MaxQueue(k)
        res = []
        for i in range(k - 1):
            mq.put(nums[i])

        for i in range(k - 1, len(nums)):
            mq.put(nums[i])
            res.append(mq.getMax())

        return res

