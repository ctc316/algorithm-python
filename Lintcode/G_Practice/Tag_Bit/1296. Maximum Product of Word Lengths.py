class Solution:
    """
    @param words: a string array
    @return: the maximum product
    """
    def maxProduct(self, words):
        n = len(words)
        if n < 2:
            return 0

        char_hashs = [0 for _ in range(n)]
        for i, word in enumerate(words):
            for ch in word:
                char_hashs[i] |= 1 << (ord(ch) - ord('a'))

        maximum = 0
        for i in range(n):
            for j in range(i, n):
                if char_hashs[i] & char_hashs[j] != 0:
                    continue

                maximum = max(maximum, len(words[i]) * len(words[j]))

        return maximum