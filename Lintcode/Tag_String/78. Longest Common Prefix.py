class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        if not strs or len(strs) == 0:
            return ""

        min_leng = float("Inf")
        for s in strs:
            min_leng = min(min_leng, len(s))

        n = len(strs)
        i = 0
        while i < min_leng:
            ch = strs[0][i]
            for j in range(1, n):
                if strs[j][i] != ch:
                    return strs[0][:i]

            i += 1

        return strs[0][:i]