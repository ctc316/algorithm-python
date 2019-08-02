class Solution:
    """
    @param str1: a given string
    @param str2: another given string
    @return: An array of missing string
    """
    def missingString(self, str1, str2):
        return [s for s in str1.split(" ") if s not in set(str2.split(" "))]
