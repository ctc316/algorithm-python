class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        candidates.sort()
        n = len(candidates)
        solutions = []
        self.dfs(candidates, n, 0, target, [], solutions)
        return solutions


    def dfs(self, candidates, n, start, target, combination, solutions):
        if target == 0:
            solutions.append([c for c in combination])
            return

        for i in range(start, n):
            if candidates[i] > target:
                break

            if i > start and candidates[i] == candidates[i - 1]:
                continue

            combination.append(candidates[i])
            self.dfs(candidates, n, i, target - candidates[i], combination, solutions)
            combination.pop()