class Solution:
    """
    @param s: the string s
    @return: check if the string is interesting
    """
    def check(self, s):
        self.visited = set()
        return 'yes' if self.dfs(s, 0) else 'no'

    def dfs(self, s, start):
        if start in self.visited:
            return False

        if start > len(s):
            return False

        if start == len(s):
            return True

        result = False
        num = 0
        i = start
        while i < len(s) and s[i].isdigit():
            num = num * 10 + ord(s[i]) - ord('0')
            result = self.dfs(s, i + num + 1)
            if result:
                return True

            i += 1

        self.visited.add(start)
        return result