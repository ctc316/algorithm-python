class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        if len(t) > len(s):
            temp = s
            s = t
            t = temp

        n = len(s)
        m = len(t)

        if n - m > 1:
            return False

        edited = False
        j = 0
        for i in range(n):
            if j == m:
                return not edited

            if s[i] != t[j]:
                if edited:
                    return False
                edited = True
                if n - 1 == m:
                    j -= 1

            j += 1

        return edited