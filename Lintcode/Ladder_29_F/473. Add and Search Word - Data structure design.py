class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def addWord(self, word):
        self.addWordHelper(word, 0, self.root)


    def addWordHelper(self, word, i, node):
        if i >= len(word):
            node.isWord = True
            return

        ch = word[i]
        if ch not in node.children:
            node.children[ch] = TrieNode()
        if '.' not in node.children:
            node.children['.'] = TrieNode()

        self.addWordHelper(word, i + 1, node.children[ch])
        self.addWordHelper(word, i + 1, node.children['.'])

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        n = len(word)
        if n == 0:
            return False

        node = self.root
        for ch in word:
            if ch not in node.children:
                return False

            node = node.children[ch]

        return node is not None and node.isWord