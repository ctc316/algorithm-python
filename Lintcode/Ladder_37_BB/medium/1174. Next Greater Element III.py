class Solution:
    """
    @param n: an integer
    @return: the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n
    """
    def nextGreaterElement(self, n):
        digits = [i for i in str(n)]
        digits.sort()
        res = self.dfs(digits, [], n)
        return res if res else -1


    def dfs(self, digits, combi, n):
        if combi and int("".join(combi)) < n // 10 ** len(digits):
            return

        if not digits:
            res = int("".join(combi))
            if res >= 2 ** 31:
                return -1
            if res > n:
                return res
            return None

        for i in range(len(digits)):
            if i > 0 and digits[i] == digits[i - 1]:
                continue
            combi.append(digits[i])
            res = self.dfs([digits[j] for j in range(len(digits)) if j != i], combi, n)
            if res:
                return res
            combi.pop()