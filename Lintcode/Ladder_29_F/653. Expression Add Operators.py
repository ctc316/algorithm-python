class Solution:
    """
    @param num: a string contains only digits 0-9
    @param target: An integer
    @return: return all possibilities
    """
    def addOperators(self, num, target):
        results = []
        self.dfs(num, target, 0, "", 0, 0, results)
        return results


    def dfs(self, num, target, start, string, summ, lastOp, results):
        if start == len(num):
            if summ == target:
                results.append(string)
            return

        for i in range(start, len(num)):
            x = num[start : i + 1]

            if start == 0:
                self.dfs(num, target, i + 1, x, int(x), int(x), results)
            else:
                self.dfs(num, target, i + 1, string + '*' + x, summ - lastOp + lastOp * int(x), lastOp * int(x), results)
                self.dfs(num, target, i + 1, string + '+' + x, summ + int(x), int(x), results)
                self.dfs(num, target, i + 1, string + '-' + x, summ - int(x), -int(x), results)

            if int(x) == 0:
                break