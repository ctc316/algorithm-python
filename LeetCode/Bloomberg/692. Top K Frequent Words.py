class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = {}
        for w in words:
            counts[w] = counts.get(w, 0) + 1

        res = sorted([(-v, k) for k, v in counts.items()])
        return [res[i][1] for i in range(k)]