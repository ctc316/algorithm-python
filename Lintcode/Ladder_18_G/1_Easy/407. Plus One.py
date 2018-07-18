class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        if len(digits) == 0:
            return digits

        digits[-1] += 1
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] == 10:
                digits[i] = 0
                digits[i - 1] += 1

        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)

        return digits