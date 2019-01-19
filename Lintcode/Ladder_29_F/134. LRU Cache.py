class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.dummy = Node(-1, 0)
        self.tail = self.dummy
        self.node_map = {}

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self.__moveToHead(node)
        return node.val

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if key not in self.node_map:
            if self.count == self.capacity:
                self.__removeTail()
            else:
                self.count += 1

            node = Node(key, value, prev=self.tail)
            self.node_map[key] = node
            self.tail.next = node
            self.tail = node

        else:
            node = self.node_map[key]
            node.val = value

        self.__moveToHead(node)


    def __removeTail(self):
        if self.tail is self.dummy:
            return

        del self.node_map[self.tail.key]
        self.tail = self.tail.prev
        self.tail.next = None


    def __moveToHead(self, node):
        if node is self.dummy.next:
            return

        if node is self.tail:
            self.tail = node.prev

        if node.next is not None:
            node.next.prev = node.prev

        if node.prev is not None:
            node.prev.next = node.next

        node.next = self.dummy.next
        node.prev = self.dummy

        if self.dummy.next:
            self.dummy.next.prev = node
        self.dummy.next = node