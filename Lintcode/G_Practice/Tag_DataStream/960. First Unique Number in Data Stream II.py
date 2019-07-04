class MyListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DataStream:
    def __init__(self):
        self.nodeMap = {}
        self.head = None
        self.tail = None

    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        if num in self.nodeMap:
            self.__removeNode(self.nodeMap[num])
        else:
            node = MyListNode(num)
            self.nodeMap[num] = node
            if not self.head:
                self.head = self.tail = node
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node

    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        if self.head:
            return self.head.val
        return None


    def __removeNode(self, node):
        if not node:
            return
        if node is self.head:
            self.head = node.next
        if node is self.tail:
            self.tail = node.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev