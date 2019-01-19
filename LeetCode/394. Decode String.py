class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        cur_str = ""
        i = 0
        while i < len(s):
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
                i += 1

            if num > 0:
                stack.append(cur_str)
                stack.append(num)
                cur_str = ""

            if s[i] == '[':
                pass
            elif s[i] == ']':
                cur_str *= int(stack.pop())
                while len(stack) > 0 and not isinstance(stack[-1], int):
                    cur_str = stack.pop() + cur_str
            else:
                cur_str += s[i]

            i += 1

        return cur_str