class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            
            elif ch == ')' or ch == '}' or ch == ']':
                if len(stack) == 0:
                    return False
                elif ch == ')' and stack[-1] == '(' or \
                     ch == '}' and stack[-1] == '{' or \
                     ch == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False

        return len(stack) == 0