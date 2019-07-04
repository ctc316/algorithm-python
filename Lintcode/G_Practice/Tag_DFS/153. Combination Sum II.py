class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        num.sort()
        n = len(num)
        solutions = []
        self.dfs(num, n, 0, target, [], solutions)
        return solutions


    def dfs(self, num, n, start, target, combination, solutions):
        if target == 0:
            solutions.append([c for c in combination])
            return

        for i in range(start, n):
            if num[i] > target:
                break

            if i > start and num[i] == num[i - 1]:
                continue

            combination.append(num[i])
            self.dfs(num, n, i + 1, target - num[i], combination, solutions)
            combination.pop()
