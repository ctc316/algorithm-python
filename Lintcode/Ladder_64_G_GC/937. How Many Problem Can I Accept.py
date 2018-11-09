class Solution:
    """
    @param n: an integer
    @param k: an integer
    @return: how many problem can you accept
    """
    def canAccept(self, n, k):
        n = int(n / k)
        start = 0
        end = n
        while start + 1 < end:
            mid = start + int((end - start) / 2)
            fact = ((1 + mid) * mid) / 2
            if fact <= n:
                start = mid
            else:
                end = mid

        if ((1 + end) * end) / 2 <= n:
            return end
        return start