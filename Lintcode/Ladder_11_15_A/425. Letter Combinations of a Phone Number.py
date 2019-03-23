class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        n = len(digits)
        if n == 0:
            return []

        res = []
        stack = [(0, "")]
        while len(stack) > 0:
            idx, string = stack.pop()
            if idx == n:
                res.append(string)
                continue

            letters = self.digitToLetters(digits[idx])
            for l in letters:
                stack.append((idx + 1, string + l))

        return res


    def digitToLetters(self, digit):
        if digit == '2':
            return ['a', 'b', 'c']
        elif digit == '3':
            return ['d', 'e', 'f']
        elif digit == '4':
            return ['g', 'h', 'i']
        elif digit == '5':
            return ['j', 'k', 'l']
        elif digit == '6':
            return ['m', 'n', 'o']
        elif digit == '7':
            return ['p', 'q', 'r', 's']
        elif digit == '8':
            return ['t', 'u', 'v']
        elif digit == '9':
            return ['w', 'x', 'y', 'z']