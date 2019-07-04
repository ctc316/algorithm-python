class Solution:
    """
    @param data: an array of integers
    @return: whether it is a valid utf-8 encoding
    """
    def validUtf8(self, data):
        if not data:
            return False

        n = len(data)
        if n == 1:
            return data[0] & 128 == 0

        # count starting 1
        byte1 = data[0]
        mask = 128
        ones = 0
        while byte1 & mask == mask:
            ones += 1
            mask >>= 1

        # check 10xxx
        for byte in data[1:ones]:
            if byte & 192 != 128:
                return False

        return True
