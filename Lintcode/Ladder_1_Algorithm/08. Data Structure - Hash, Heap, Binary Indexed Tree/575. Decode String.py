class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        return self.dfs(s, 1)

    def dfs(self, s, multiply):
        n = len(s)
        string = ""
        i = 0
        while i < n:
            if s[i].isdigit():
                # check for multiply
                left = i + 1
                while left < n and s[left].isdigit():
                    left += 1

                mul = int(s[i:left])

                # find the close parenthess
                open = 0
                right = left
                while right < n:
                    if s[right] == '[':
                        open += 1
                    elif s[right] == ']':
                        open -= 1
                        if open == 0:
                            break
                    right += 1

                string += self.dfs(s[left + 1 : right], mul)
                i = right + 1

            else:
                string += s[i]
                i += 1

        return string * multiply