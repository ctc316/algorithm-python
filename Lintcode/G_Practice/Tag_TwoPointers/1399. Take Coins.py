class Solution:
    """
    @param list: The coins
    @param k: The k
    @return: The answer
    """
    def takeCoins(self, list, k):
        n = len(list)
        if k >= n:
            return sum(list)

        cur = sum(list[n - k:])
        maxi = cur
        for start in range(n - k, n + 1):
            start %= n
            end = (start + k) % n
            cur = cur - list[start] + list[end]
            maxi = max(maxi, cur)

        return maxi
