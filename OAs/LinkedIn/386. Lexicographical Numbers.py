class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        results = []
        for i in range(1, 10):
            self.dfs(n, i, results)

        return results

    def dfs(self, n, prefix, results):
        if prefix > n:
            return

        results.append(prefix)
        prefix *= 10
        for i in range(10):
            if prefix + i > n:
                return

            self.dfs(n, prefix + i, results)