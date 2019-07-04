class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        '''
        8 1 0
        6 9
        '''

        s = str(num)
        n = len(s)

        j = n // 2
        i = j if n % 2 == 1 else j - 1

        for _ in range(i + 1):
            if not (s[i] == '6' and s[j] == '9' or s[i] == '9' and s[j] == '6') and \
              (s[i] != s[j] or s[i] != '0' and s[i] != '1' and s[i] != '8'):
                return False

            i -= 1
            j += 1

        return True