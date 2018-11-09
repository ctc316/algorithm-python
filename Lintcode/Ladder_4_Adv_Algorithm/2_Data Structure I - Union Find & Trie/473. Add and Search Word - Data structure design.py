class TrieNode:
    def __init__(self):
        self.children = {} # char: TrieNode
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def addWord(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.is_word = True

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        n = len(word)
        if n == 0:
            return False

        stack = []
        stack.append((0, self.root))
        while len(stack) > 0:
            idx, node = stack.pop()
            if idx == n:
                if node.is_word:
                    return True
                continue

            ch = word[idx]

            if ch == '.':
                for val in node.children.values():
                    stack.append((idx + 1, val))
            elif ch in node.children:
                    stack.append((idx + 1, node.children[ch]))

        return False