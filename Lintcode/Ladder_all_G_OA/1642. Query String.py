class Solution:
    """
    @param str: the string
    @param n: the n
    @return: yes or no
    """
    def queryString(self, str, n):
        for i in range(n, -1, -1):
            if not '{0:0b}'.format(i) in str:
                return 'no'

        return 'yes'



class Solution:
    """
    @param str: the string
    @param n: the n
    @return: yes or no
    """
    def queryString(self, str, n):
        found = [False for _ in range(n + 1)]
        for i in range(len(str)):
            for j in range(i + 1, len(str) + 1):
                integer = int(str[i:j], 2)
                if integer < n + 1:
                    found[integer] = True

        for res in found:
            if not res:
                return 'no'

        return 'yes'