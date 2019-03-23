class Solution:
    """
    @param str: A string
    @return: An integer
    """
    def atoi(self, str):
        str = str.strip()
        n = len(str)
        if n == 0:
            return 0

        isNeg = False
        start = 0
        if str[0] == '-':
            isNeg = True
            start = 1
        elif str[0] == '+':
            start = 1

        inPrecision = False
        num = 0.0
        precision = 1
        for i in range(start, n):
            ch = str[i]
            if ch == '.':
                if inPrecision:
                    break
                inPrecision = True
                continue

            if not ch.isdigit():
                break

            d = ord(ch) - ord('0')
            if inPrecision:
                precision *= 10

            num *= 10
            num += d

        num /= precision
        if int(num) == num:
            num = int(num)

        if isNeg:
            num = -num

        if num < -2147483648:
            return -2147483648

        if num > 2147483647:
            return 2147483647

        return num