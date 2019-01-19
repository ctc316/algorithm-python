"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""

class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = nestedList

    # @return {int} the next element in the iteration
    def next(self):
        return self.stack.pop().getInteger()

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        if len(self.stack) == 0:
            return False
        next_node = self.stack[-1]
        if next_node.isInteger():
            return True
        else:
            self.stack.pop()
            for node in reversed(next_node.getList()):
                self.stack.append(node)
            return self.hasNext()


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())