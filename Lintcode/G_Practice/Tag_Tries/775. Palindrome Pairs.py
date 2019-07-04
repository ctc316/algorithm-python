class Solution:
    """
    @param words: a list of unique words
    @return: all pairs of distinct indices
    """
    def palindromePairs(self, words):
        res = []
        table = {}
        if not words:
            return res

        for index, word in enumerate(words):
            table[word] = index

        for index, word in enumerate(words):
            for i in range(len(word) + 1):
                left, right = word[:i], word[i:]

                if self.isPal(left):
                    reversedRight = right[::-1]
                    if reversedRight in table and table[reversedRight] != index:
                        res.append([table[reversedRight], index])

                if len(right) > 0 and self.isPal(right):
                    reversedLeft = left[::-1]
                    if reversedLeft in table and table[reversedLeft] != index:
                        res.append([index, table[reversedLeft]])
        return res

    def isPal(self, s):
        return s == s[::-1]