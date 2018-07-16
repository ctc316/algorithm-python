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

# Version 1: 先處理
class NestedIterator(object):

    def __init__(self, nestedList):
        self.index = 0
        self.flattened = self.dfs(nestedList)
        self.n = len(self.flattened)


    # @return {int} the next element in the iteration
    def next(self):
        self.index += 1
        return self.flattened[self.index - 1]


    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        return self.index < self.n


    def dfs(self, nestedList):
        flattened = []
        for n in nestedList:
            if n.isInteger():
                flattened.append(n.getInteger())
            else:
                flattened.extend(self.dfs(n.getList()))
        return flattened


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


# Version 2: Stack 紀錄位置
class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = [[nestedList, 0]]
        
    # @return {int} the next element in the iteration
    def next(self):
        self.hasNext()
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[i].getInteger()
        
    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        s = self.stack
        while s:
            nestedList, i = s[-1]
            if i == len(nestedList):
                s.pop()
            else:
                x = nestedList[i]
                if x.isInteger():
                    return True
                s[-1][1] += 1
                s.append([x.getList(), 0])
        return False