class Solution:
    """
    @param s: the string that represents a number
    @return: whether the string is a valid number
    """
    def isNumber(self, s):
        s = s.strip()
        if len(s) == 0:
            return False

        if s[0] == '+' or s[0] == '-':
            s = s[1:]

        pow_parts = s.split('e')
        if len(pow_parts) > 2:
            return False

        if len(pow_parts[0]) == 0:
            return False

        if len(pow_parts) == 2:
            if len(pow_parts[1]) == 0:
                return False
            for ch in pow_parts[1]:
                if not self.isDigit(ch):
                    return False

        base_parts = pow_parts[0].split('.')
        if len(base_parts) > 2:
            return False

        if len(base_parts) == 2:
            if len(base_parts[0]) == 0 and len(base_parts[1]) == 0:
                return False

            for ch in base_parts[1]:
                if not self.isDigit(ch):
                    return False

        for ch in base_parts[0]:
            if not self.isDigit(ch):
                return False

        return True


    def isDigit(self, ch):
        if ord(ch) < ord('0') or ord(ch) > ord('9'):
            return False
        return True