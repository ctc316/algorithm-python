class Solution:
    """
    @param str: The input string
    @return: The answer
    """
    def dataSegmentation(self, str):
        results = []
        word = ""
        for ch in str:
            if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
                word += ch
                continue

            if len(word) > 0:
                results.append(word)
                word = ""

            if ch != " ":
                results.append(ch)

        if len(word) > 0:
            results.append(word)

        return results