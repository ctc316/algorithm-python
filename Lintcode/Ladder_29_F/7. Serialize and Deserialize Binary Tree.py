"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        if root is None:
            return ''

        results = []
        from queue import Queue
        q = Queue()
        q.put(root)

        while not q.empty():
            for _ in range(q.qsize()):
                node = q.get()
                results.append(str(node.val))

                if node.val != '#':
                    q.put(node.left if node.left else TreeNode('#'))
                    q.put(node.right if node.right else TreeNode('#'))

        i = len(results)
        while i > 0 and results[i - 1] == '#':
            i -= 1

        return ','.join(results[:i])

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    """
    def deserialize(self, data):
        if len(data) == 0:
            return None

        data = data.split(',')
        n = len(data)
        idx = 0

        from queue import Queue
        q = Queue()

        root = TreeNode(data[0])
        q.put(root)

        while idx < n and not q.empty():
            node = q.get()

            idx += 1
            if idx < n and data[idx] != '#':
                node.left = TreeNode(data[idx])
                q.put(node.left)

            idx += 1
            if idx < n and data[idx] != '#':
                node.right = TreeNode(data[idx])
                q.put(node.right)

        return root