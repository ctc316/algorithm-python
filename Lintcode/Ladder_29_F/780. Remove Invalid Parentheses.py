class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        min_left, min_right = self.minimumRemove(s)
        if min_left == 0 and min_right == 0:
            return [s]

        self.s = s
        self.n = len(s)
        self.results = []

        self.DFS(0, "", 0, min_left, min_right)

        if len(self.results) == 0:
            return [""]
        return self.results


    def DFS(self, start, cur_str, left, left_remove, right_remove):
        if self.n - start < left_remove + right_remove:
            return

        for i in range(start, self.n):
            if self.s[i] == '(':
                if left_remove > 0 and (i == start or self.s[i] != self.s[i - 1]):
                    self.DFS(i + 1, cur_str, left, left_remove - 1, right_remove)
                left += 1

            elif self.s[i] == ')':
                if right_remove > 0 and (i == start or self.s[i] != self.s[i - 1]):
                    self.DFS(i + 1, cur_str, left, left_remove, right_remove - 1)
                left -= 1
                if left < 0:
                    return

            cur_str += self.s[i]

        if left == 0:
            self.results.append(cur_str)


    def minimumRemove(self, s):
        left = 0
        right = 0

        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left == 0:
                    right += 1
                else:
                    left -= 1

        return left, right