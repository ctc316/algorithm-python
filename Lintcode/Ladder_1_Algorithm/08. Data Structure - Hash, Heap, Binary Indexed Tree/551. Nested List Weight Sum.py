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


# Version 1: DFS Recursive
class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        return self.dfs(nestedList, 1)

    def dfs(self, nestedList, depth):
        sum = 0
        for item in nestedList:
            if item.isInteger():
                sum += item.getInteger() * depth
            else:
                sum += self.dfs(item.getList(), depth + 1)

        return sum




# Version 2: BFS, Non-Recursive
class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        if len(nestedList) == 0:
            return 0

        from queue import Queue
        q = Queue()
        sum = 0
        depth = 1

        for item in nestedList:
            q.put(item)

        while not q.empty():
            for _ in range(q.qsize()):
                item = q.get()
                if item.isInteger():
                    sum += item.getInteger() * depth
                else:
                    for next in item.getList():
                        q.put(next)
            depth += 1

        return sum