"""
Definition of TrieNode:
class TrieNode:
    def __init__(self):
        # <key, value>: <Character, TrieNode>
        self.children = collections.OrderedDict()
"""


class Solution:

    '''
    @param root: An object of TrieNode, denote the root of the trie.
    This method will be invoked first, you should design your own algorithm
    to serialize a trie which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        if not root:
            return ""

        ret = "<"
        for k, v in root.children.items():
            ret += k + self.serialize(v)
        ret += ">"
        return ret


    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    '''
    def deserialize(self, data):
        if not data:
            return None

        root = TrieNode()
        cur = root
        stack = []
        for ch in data:
            if ch == '<':
                stack.append(cur)
            elif ch == '>':
                stack.pop()
            else:
                cur = TrieNode()
                stack[-1].children[ch] = cur

        return root
