'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ),
the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Do not use the eval built-in library function.

Example
Example 1

Input："1 + 1"
Output：2
Example 2

Input："(1+(4+5+2)-3)+(6+8)"
Output：23

'''

'''
(+(++
1 4 5 2

( + - )
1 11 3

+( + )
9 6 8
'''


class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        op_stack = []
        num_stack = []

        n = len(s)
        i = 0
        while i < n:
            num = 0
            foundNum = False
            while i < n and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
                foundNum = True
            if foundNum:
                num_stack.append(num)

            if i >= n:
                break
            ch = s[i]
            if ch == ' ':
                i += 1
                continue

            if ch == ')':
                res = 0
                while len(op_stack) > 0:
                    op = op_stack.pop()
                    num = num_stack.pop()
                    if op == '-':
                        res -= num
                    else:
                        res += num
                    if op == '(':
                        break
                num_stack.append(res)
            else:
                op_stack.append(ch)

            i += 1

        res = 0
        while len(num_stack) > 0:
            num = num_stack.pop()
            if len(op_stack) > 0 and op_stack.pop() == '-':
                res -= num
            else:
                res += num

        return res