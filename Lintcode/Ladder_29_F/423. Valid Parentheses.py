class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        stack = []
        for ch in s:
            if ch == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            elif ch == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
            elif ch == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            else:
                stack.append(ch)
    
        return len(stack) == 0