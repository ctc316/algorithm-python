class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        stack = []
        cur_str = ""
        i = 0
        while i < len(s):
            num = ""
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i += 1

            if len(num) > 0:
                stack.append(cur_str)
                cur_str = ""
                stack.append(num)

            if s[i] == '[':
                pass
            elif s[i] == ']':
                cur_str *= int(stack.pop())
                while len(stack) > 0 and not stack[-1].isdigit():
                    cur_str = stack.pop() + cur_str
            else:
                cur_str += s[i]

            i += 1

        return cur_str