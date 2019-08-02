class Trie:
    class TrieNode:
        def __init__(self):
            self.children = [None for i in range(26)]
            self.is_word = False


    def __init__(self):
        self.root =self.TrieNode()

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = self.TrieNode()
            node = node.children[idx]
        node.is_word = True


    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        return node.is_word


    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        return True
