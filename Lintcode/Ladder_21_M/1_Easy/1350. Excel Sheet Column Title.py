class Solution:
    """
    @param n: a integer
    @return: return a string
    """
    def convertToTitle(self, n):
        result = ""
        while n > 0:
            mod = n % 26
            if mod == 0:
                mod = 26
            result = chr(mod + 64) + result
            n = int((n - mod) / 26)

        return result