class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

        for i in range(n):
            is_palindrome[i][i] = True

        for i in range(n - 1):
            is_palindrome[i][i + 1] = s[i] == s[i + 1]

        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and s[i] == s[j]

        results = []
        self.dfs(s, 0, is_palindrome, [], results)
        return results


    def dfs(self, s, start, is_palindrome, combi, results):
        if start == len(s):
            results.append([c for c in combi])
            return

        for end in range(start, len(s)):
            if not is_palindrome[start][end]:
                continue

            combi.append(s[start:end + 1])
            self.dfs(s, end + 1, is_palindrome, combi, results)
            combi.pop()