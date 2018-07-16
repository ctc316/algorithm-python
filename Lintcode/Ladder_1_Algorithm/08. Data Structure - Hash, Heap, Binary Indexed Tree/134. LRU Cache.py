class LRUListNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash = {}      # store the prev node
        self.head = self.tail = LRUListNode() # dummy
        self.size = 0


    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key in self.hash:
            self.moveToTail(key)
            return self.hash[key].next.value
        else:
            return -1

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if key in self.hash:
            self.moveToTail(key)
            self.hash[key].next.value = value
        else:
            # add new node
            node = LRUListNode(key, value)
            self.pushBack(node)
            self.size += 1

            # check size and delete the front one (LRU)
            if len(self.hash) > self.capacity:
                del self.hash[self.head.next.key]
                self.head.next = self.head.next.next
                self.hash[self.head.next.key] = self.head


    def moveToTail(self, key):
        # find nodePrev
        nodePrev = self.hash[key]
        if nodePrev.next is self.tail:
            return

        # get the node and cut off the node's link
        node = nodePrev.next
        nodePrev.next = nodePrev.next.next
        self.hash[nodePrev.next.key] = nodePrev

        # push to back
        self.pushBack(node)


    def pushBack(self, node):
        self.hash[node.key] = self.tail
        self.tail.next = node
        self.tail = self.tail.next