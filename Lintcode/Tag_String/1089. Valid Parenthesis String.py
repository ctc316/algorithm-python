# Version 1: DFS, TLE
class Solution:
    """
    @param s: the given string
    @return: whether this string is valid
    """
    def checkValidString(self, s):
        return self.dfs(s, 0, 0)

    def dfs(self, s, idx, left_count):
        if left_count < 0:
            return False

        if idx == len(s):
            return left_count == 0

        if s[idx] == "*":
            return self.dfs(s, idx + 1, left_count + 1) or \
                   self.dfs(s, idx + 1, left_count - 1) or \
                   self.dfs(s, idx + 1, left_count)

        if s[idx] == "(":
            left_count += 1

        if s[idx] == ")":
            left_count -= 1

        return self.dfs(s, idx + 1, left_count)




# Version 2: logic
# https://www.jiuzhang.com/solution/valid-parenthesis-string/
class Solution:
    """
    @param s: the given string
    @return: whether this string is valid
    """
    def checkValidString(self, s):
        unpair_left = 0
        avail_left = 0
        for ch in s:
            if ch == "(":
                unpair_left += 1
                avail_left += 1

            elif ch == "*":
                if unpair_left > 0:
                    unpair_left -= 1
                avail_left += 1

            else:
                if unpair_left > 0:
                    unpair_left -= 1
                avail_left -= 1
                if avail_left < 0:
                    return False

        return unpair_left == 0
