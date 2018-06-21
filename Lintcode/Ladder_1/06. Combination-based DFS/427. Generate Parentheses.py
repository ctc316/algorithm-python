class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        results = []
        self.dfs(n, n, 0, "", results)
        return results


    def dfs(self, left, right, unclosed, sol, results):
        if left == 0 and right == 0:
            results.append(sol)

        if left > 0:
            self.dfs(left - 1, right, unclosed + 1, sol + "(", results)

        if unclosed > 0 and right > 0:
            self.dfs(left, right - 1, unclosed - 1, sol + ")", results)