class Solution:
    """
    @param str: a string
    @return: a compressed string
    """
    def compress(self, str):
        result = ""
        prev_ch = ""
        count = 0
        for ch in str:
            if ch != prev_ch and count > 0:
                result += prev_ch + count.__str__()
                count = 0

            prev_ch = ch
            count += 1

        result += prev_ch + count.__str__()

        if len(result) >= len(str):
            return str

        return result