class ValidWordAbbr:
    """
    @param: dictionary: a list of words
    """
    def __init__(self, dictionary):
        self.dict = set(dictionary)
        self.abbrs = {}
        for word in self.dict:
            a = self.abbreviate(word)
            self.abbrs[a] = self.abbrs[a] + 1 if a in self.abbrs else 1


    """
    @param: word: a string
    @return: true if its abbreviation is unique or false
    """
    def isUnique(self, word):
        a = self.abbreviate(word)
        return a not in self.abbrs or word in self.dict and self.abbrs[a] == 1

    def abbreviate(self, word):
        return word if len(word) < 2 else word[0] + str(len(word) - 2) + word[-1]

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param = obj.isUnique(word)