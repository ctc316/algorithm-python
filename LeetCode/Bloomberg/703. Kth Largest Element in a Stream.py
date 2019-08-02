from bisect import insort

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = sorted(nums)
        self.k = k


    def add(self, val: int) -> int:
        insort(self.arr, val)
        if len(self.arr) >= self.k:
            return self.arr[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)