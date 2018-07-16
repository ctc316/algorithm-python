class Pair:
    def __init__(self, idx, val):
        self.idx = idx
        self.val = val

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        if len(nums) < 2:
            return []

        if target < 0:
            target = -target

        n = len(nums)
        pairs = []
        for i in range(n):
            pairs.append(Pair(i, nums[i]))

        pairs.sort()

        p2 = 1
        for p1 in range(n - 1):
            if p1 == p2:
                p2 += 1

            while p2 < n and pairs[p2].val - pairs[p1].val < target:
                p2 += 1

            if p2 < n and pairs[p2].val - pairs[p1].val == target:
                result = [pairs[p1].idx + 1, pairs[p2].idx + 1]
                if result[0] < result[1]:
                    return result
                return [result[1], result[0]]

        return []