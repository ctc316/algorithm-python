class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {}
        self.head = None
        self.tail = None


    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1

        node = self.mapping[key]
        self.__moveToHead(node)
        return node.val


    def put(self, key: int, value: int) -> None:
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
        del self.mapping[self.tail.key]

        if self.tail.prev:
            self.tail.prev.next = None
        self.tail = self.tail.prev



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)