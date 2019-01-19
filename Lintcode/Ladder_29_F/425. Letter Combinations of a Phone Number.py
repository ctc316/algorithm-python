class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []

        results = []
        self.DFS(digits, 0, '', results)
        return results


    def DFS(self, digits, idx, string, results):
        if idx == len(digits):
            results.append(string)
            return

        for ch in self.digitToLetters(digits[idx]):
            self.DFS(digits, idx + 1, string + ch, results)


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