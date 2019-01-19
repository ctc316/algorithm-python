class Solution:
    """
    @param length: the length of board
    @param connections: the connections of the positions
    @return: the minimum steps to reach the end
    """
    def modernLudo(self, length, connections):
        if length <= 1:
            return 0

        conn_map = {}
        for c in connections:
            conn_map[c[0]] = c[1]

        dp = [sys.maxsize for _ in range(length + 1)]
        dp[1] = 0

        for i in range(2, length + 1):
            for j in range(max(1, i - 6), i):
                dp[i] = min(dp[i], dp[j] + 1)

            if i in conn_map:
                dp[conn_map[i]] = min(dp[conn_map[i]], dp[i])

        return dp[-1]