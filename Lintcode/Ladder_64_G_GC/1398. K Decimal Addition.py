class Solution:
    """
    @param k: The k
    @param a: The A
    @param b: The B
    @return: The answer
    """
    def addition(self, k, a, b):
        result = ""
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 and j >= 0:
            summ = carry + ord(a[i]) - ord('0') + ord(b[j]) - ord('0')
            carry = int(summ / k)
            result += str(summ % k)
            i -= 1
            j -= 1

        while i >= 0 :
            summ = carry + ord(a[i]) - ord('0')
            carry = int(summ / k)
            result += str(summ % k)
            i -= 1

        while j >= 0 :
            summ = carry + ord(b[j]) - ord('0')
            carry = int(summ / k)
            result += str(summ % k)
            j -= 1

        if carry > 0:
            result += str(carry)


        result = result[::-1]

        # trim zeros
        for i in range(len(result)):
            if result[i] != "0":
                return result[i:]

        return "0"