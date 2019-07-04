class Node:
    def __init__(self, key="", val=-1, prev=None, next=None):
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
        self.mapping = {}
        self.head = None
        self.tail = None

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.mapping:
            return -1

        node = self.mapping[key]
        self.__moveToHead(node)
        return node.val


    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if key not in self.mapping:
            if len(self.mapping) >= self.capacity:
                self.__removeTail()

            new_node = Node(key, value, None, self.head)
            self.mapping[key] = new_node

            if self.head:
                self.head.prev = new_node
            self.head = new_node

            if self.tail is None:
                self.tail = self.head

        else:
            node = self.mapping[key]
            node.val = value
            self.__moveToHead(node)


    def __moveToHead(self, node):
        if node is self.head:
            return

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        if node is self.tail:
            self.tail = node.prev

        self.head.prev = node
        node.next = self.head
        self.head = node


    def __removeTail(self):
        if self.tail.prev:
            self.tail.prev.next = None

        del self.mapping[self.tail.key]
        self.tail = self.tail.prev
    