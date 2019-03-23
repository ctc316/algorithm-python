class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        counter = {}
        for c in str:
            counter[c] = counter.get(c, 0) + 1

        for c in str:
            if counter[c] == 1:
                return c


                

class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        uniques = set()
        occurs = set()
        for s in str:
            if s in uniques:
                uniques.remove(s)
            elif s not in occurs:
                uniques.add(s)
            occurs.add(s)

        for s in str:
            if s in uniques:
                return s

        return ''