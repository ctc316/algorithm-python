class Solution:
    """
    @param target: the target string
    @param s:
    @return: output all strings containing target  in s
    """
    def getAns(self, target, s):
        res = []
        for word in s:
            if self.subseqence(word, target):
                res.append(word)

        return res


    def subseqence(self, word, target):
        n = len(word)
        m = len(target)
        if n < m:
            return False

        i = 0
        j = 0
        while i < n and j < m:
            if word[i] == target[j]:
                j += 1
            i += 1

        return j == len(target)