class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        return " ".join(list(filter(lambda x: x != "", s.split(" ")))[::-1])