class Solution:
    """
    @param n: a positive integer
    @return: the minimum number of replacements
    """
    def integerReplacement(self, n):
        self.records = {}
        steps = self.dfs(n)
        return steps

    def dfs(self, n):
        if n == 1:
            return 0

        if n in self.records:
            return self.records[n]

        if n % 2 == 0:
            self.records[n] = self.dfs(n / 2) + 1
        else:
            self.records[n] = min(self.dfs(n + 1), self.dfs(n - 1)) + 1

        return self.records[n]