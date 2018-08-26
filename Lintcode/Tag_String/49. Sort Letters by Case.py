class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars):
        pos = 0
        for i in range(len(chars)):
            if ord(chars[i]) >= 97:
                temp = chars[i]
                chars[i] = chars[pos]
                chars[pos] = temp
                pos += 1