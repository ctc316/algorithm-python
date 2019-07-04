class Solution:
    """
    @param n: a non-negative integer
    @return: the total number of full staircase rows that can be formed
    """
    def arrangeCoins(self, n):
        start = 0
        end = n
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid * (mid + 1) // 2 > n:
                end = mid
            else:
                start = mid

        if end * (end + 1) // 2 <= n:
            return end
        return start