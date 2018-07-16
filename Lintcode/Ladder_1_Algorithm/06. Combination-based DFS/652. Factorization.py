import math

class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        results = []
        self.dfs(n, 2, [], results)
        return results


    def dfs(self, n, start, combination, results):
        if n <= 1:
            if len(combination) > 1:
                results.append(combination[:])

        for i in range(start, int(math.sqrt(n) + 1)):
            if n % i == 0:
                combination.append(i)
                self.dfs(int(n / i), i, combination, results)
                combination.pop()

        # since "1" is not in the range, we have to deal with the number itself
        if n >= start:
            combination.append(n)
            self.dfs(1, n, combination, results)
            combination.pop()