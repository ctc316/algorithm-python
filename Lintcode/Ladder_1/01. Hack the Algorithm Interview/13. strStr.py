# Brute Froce, Time: O(n^2)
class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """
    def strStr(self, source, target):
        if source is None or target is None:
            return -1

        if len(target) == 0:
            return 0

        for i in range(len(source)):
            found = True
            for j in range(len(target)):
                if i + j >= len(source) or source[i + j] != target[j]:
                    found = False
                    break

            if found:
                return i

        return -1