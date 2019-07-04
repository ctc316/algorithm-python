class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0
        self.summ = 0

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        path = []
        cur = self.root
        for ch in key:
            path.append(cur)
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]

        diff = val - cur.val
        cur.summ += diff
        cur.val = val
        for p in path:
            p.summ += diff


    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return 0
            cur = cur.children[ch]
        return cur.summ


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)