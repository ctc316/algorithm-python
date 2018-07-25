# Version 1: Naive
class Solution:
	"""
    @param str: a string
    @return: return a string
    """
    def reverseWords(self, str):
        return " ".join(str.split(" ")[::-1])