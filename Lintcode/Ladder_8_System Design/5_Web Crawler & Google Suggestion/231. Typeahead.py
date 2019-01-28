class Typeahead:
    """
    @param: dict: A dictionary of words dict
    """
    def __init__(self, dict):
        self.invertedDict = {}
        for item in dict:
            lower_item = item.lower()
            for start in range(0, len(item)):
                for end in range(start, len(item) + 1):
                    part = lower_item[start:end]
                    if part not in self.invertedDict:
                        self.invertedDict[part] = set()
                    self.invertedDict[part].add(item)

        for k, v in self.invertedDict.items():
            self.invertedDict[k] = sorted(v)

    """
    @param: str: a string
    @return: a list of words
    """
    def search(self, str):
        str = str.lower()
        if str not in self.invertedDict:
            return []
        return self.invertedDict[str]