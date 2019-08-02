class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        return " ".join([w for w in s.strip().split()[::-1]])