class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        results = []
        for i in range(len(s) - 1):
            if s[i:i + 2] == "++" :
                results.append(s[:i] + "--" + s[i + 2:])

        return results