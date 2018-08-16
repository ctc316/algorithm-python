class Solution:
    """
    @param s: string S
    @param t: string T
    @return: whether S can convert to T
    """
    def canConvert(self, s, t):
        i = 0
        j = 0
        s_len = len(s)
        t_len = len(t)
        while j < t_len:
            while i < s_len and s[i] != t[j]:
                i += 1

            if i == s_len:
                break

            i += 1
            j += 1


        return j == t_len