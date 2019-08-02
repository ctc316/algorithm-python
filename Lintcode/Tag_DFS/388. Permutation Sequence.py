class Solution:
    """
    @param n: n
    @param k: the k th permutation
    @return: return the k-th permutation
    """
    def getPermutation(self, n, k):
        self.k = k
        return self.dfs([i + 1 for i in range(n)], "")

    def dfs(self, options, combi):
        if not options:
            self.k -= 1
            if self.k == 0:
                return combi

        for i in range(len(options)):
            combi += str(options[i])
            temp = options.pop(i)
            result = self.dfs(options, combi)
            combi = combi[:-1]
            options.insert(i, temp)

            if result:
                return result