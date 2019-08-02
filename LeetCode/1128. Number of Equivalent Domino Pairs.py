class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = {}
        for d in dominoes:
            key = "{}_{}".format(sum(d), sorted(d)[0])
            if key not in counts:
                counts[key] = 1
            else:
                counts[key] += 1

        pairs = 0
        for k, v in counts.items():
            pairs += v * (v - 1) // 2
        return pairs