class Solution:
    """
    @param a: a number
    @param b: a number
    @return: the result
    """
    def addBinary(self, a, b):
        a_len = len(a)
        b_len = len(b)
        a_i = a_len - 1
        b_i = b_len - 1
        carry = 0
        result = ""
        while a_i >= 0 or b_i >= 0 or carry > 0:
            summ = carry
            if a_i >= 0:
                summ += ord(a[a_i]) - ord('0')
                a_i -= 1
            if b_i >= 0:
                summ += ord(b[b_i]) - ord('0')
                b_i -= 1

            if summ >= 2:
                summ -= 2
                carry = 1
            else:
                carry = 0

            result = str(summ) + result

        return result