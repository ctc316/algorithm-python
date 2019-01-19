class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        self.records = {}
        return self.DFS(s, p)


    def DFS(self, s, p):
        key = s + "_" + p
        if key in self.records:
            return self.records[key]

        n = len(s)
        m = len(p)
        if m == 0:
            return n == m

        if p[-1] == '*':
            if m == 1:
                result = False
            else:
                replace_ch = p[-2]
                result = self.DFS(s, p[:-2])
                for i in range(1, n + 1):
                    if result or not (replace_ch == '.' or s[-i] == replace_ch):
                        break

                    result = self.DFS(s[0:-i], p[:-2])

        elif p[-1] == '.':
            result = n != 0 and self.DFS(s[:-1], p[:-1])

        else:
            result = n != 0 and s[-1] == p[-1] and self.DFS(s[:-1], p[:-1])

        self.records[key] = result
        return result