"""
Definition of TrieNode:
class TrieNode:
    def __init__(self):
        # <key, value>: <Character, TrieNode>
        self.children = collections.OrderedDict()
        self.top10 = []
"""
class TrieService:

    def __init__(self):
        self.root = TrieNode()

    def get_root(self):
        # Return root of trie root, and
        # lintcode will print the tree struct.
        return self.root

    # @param {str} word a string
    # @param {int} frequency an integer
    # @return nothing
    def insert(self, word, frequency):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()

            node = node.children[w]
            node.top10.append(frequency)
            node.top10.sort(reverse=True)
            if len(node.top10) > 10:
                del node.top10[-1]