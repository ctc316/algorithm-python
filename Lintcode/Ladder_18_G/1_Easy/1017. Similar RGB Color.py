class Solution:
    """
    @param color: the given color
    @return: a 7 character color that is most similar to the given color
    """
    def similarRGB(self, color):
        from bisect import bisect_left
        refs = [i * 16 + i for i in range(16)]
        output = "#"
        for i in range(1, 6, 2):
            code = int(color[i:i + 2], 16)
            idx = bisect_left(refs, code)
            if idx + 1 < len(refs) and abs(code - refs[idx]) < (code - refs[idx + 1]):
                idx += 1

            output += str(hex(refs[idx]))[2:]
        return output