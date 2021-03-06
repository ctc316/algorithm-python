class Solution:
    """
    @param s: Roman representation
    @return: an integer
    """
    def romanToInt(self, s):
        n = len(s)
        result = 0
        i = 0
        while i < n:
            cumulate = 0
            j = i + 1
            curr = self.romanCharToInt(s[i])
            next = 0
            while j < n:
                next = self.romanCharToInt(s[j])
                if curr >= next:
                    break

                cumulate += curr
                curr = next
                j += 1

            result += curr - cumulate
            i = j

        return result


    def romanCharToInt(self, ch):
        if ch == 'I':
            return 1
        if ch == 'V':
            return 5
        if ch == 'X':
            return 10
        if ch == 'L':
            return 50
        if ch == 'C':
            return 100
        if ch == 'D':
            return 500
        if ch == 'M':
            return 1000