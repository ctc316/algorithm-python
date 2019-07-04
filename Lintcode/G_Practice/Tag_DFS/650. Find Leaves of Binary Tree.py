"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        layerNodes = {}
        height = self.getLayerNodesHeight(root, layerNodes)
        result = []
        for i in range(height + 1):
            result.append(layerNodes[i])
        return result


    def getLayerNodesHeight(self, node, layerNodes):
        if node is None:
            return -1
        left = self.getLayerNodesHeight(node.left, layerNodes)
        right = self.getLayerNodesHeight(node.right, layerNodes)
        height = max(left, right) + 1
        if height in layerNodes:
            layerNodes[height].append(node.val)
        else:
            layerNodes[height] = [node.val]
        return height