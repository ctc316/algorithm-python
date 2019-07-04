class BitTrieNode:
    def __init__(self, val='0', isString=False):
        self.val = val
        self.isString = isString
        self.children = [None] * 2

class Solution:
    """
    @param s: the list of binary string
    @return: the max distance
    """
    def getAns(self, s):
        root = self.buildTree(s)
        self.max_distance = 0
        self.get_max_length(root)
        return self.max_distance


    def buildTree(self, s):
        root = BitTrieNode()
        for string in s:
            cur = root
            for ch in string:
                if not cur.children[int(ch)]:
                    cur.children[int(ch)] = BitTrieNode(ch)
                cur = cur.children[int(ch)]
            cur.isString = True
        return root


    def get_max_length(self, root):
        if root is None:
            return 0
        max_length = [self.get_max_length(c) for c in root.children]

        if root.children[0] and root.children[1]:
            self.max_distance = max(self.max_distance, sum(max_length))
        if root.isString:
            self.max_distance = max(self.max_distance, max(max_length))

        return max(max_length) + 1