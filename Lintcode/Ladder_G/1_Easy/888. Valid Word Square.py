class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        for i in range(int(len(words) / 2)):
            for j in range(len(words[i])):
                if words[i][j] != words[j][i]:
                    return False

        return True