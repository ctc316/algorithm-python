class Solution:
    """
    @param S:
    @return: nothing
    """
    def toGoatLatin(self, S):
        result = []
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for i, word in enumerate(S.split(" ")):
            if word.lower()[0] in vowels:
                result.append(word + "ma" + "a" * (i + 1))
            else:
                result.append(word[1:] + word[0] + "ma" + "a" * (i + 1))

        return " ".join(result)