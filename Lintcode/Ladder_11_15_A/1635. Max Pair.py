class Solution:
    """
    @param a: the first list
    @param b: the second list
    @param x: the max sum
    @return: the pairs whose sum are not exceed x
    """
    def getAns(self, a, b, x):
        a.sort()
        b.sort()
        maxi = 0
        maxi_pairs = []
        from bisect import bisect_right
        for i in range(len(a)):
            if i > 0 and a[i] == a[i - 1]:
                continue

            target = x - a[i]
            pos = bisect_right(b, target)
            if pos == len(b) or b[pos] > target:
                pos -= 1

            if b[pos] <= target:
                pair_sum = b[pos] + a[i]
                if pair_sum == maxi:
                    maxi_pairs.append([a[i], b[pos]])
                elif pair_sum > maxi:
                    maxi = pair_sum
                    maxi_pairs = [[a[i], b[pos]]]

        return maxi_pairs