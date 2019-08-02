class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        res = sorted([(-v, k) for k, v in counts.items()])
        return [res[i][1] for i in range(k)]