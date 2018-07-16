import random
class LoadBalancer:
    def __init__(self):
        self.prevNodeMap = {}
        self.head = ListNode(0)  # dummy
        self.tail = self.head
        self.count = 0

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        if server_id in self.prevNodeMap:
            return

        # add to tail and record on map
        self.tail.next = ListNode(server_id)
        self.prevNodeMap[server_id] = self.tail
        self.tail = self.tail.next
        self.count += 1


    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        if server_id not in self.prevNodeMap:
            return

        # change the next pointer and update map or tail
        prev = self.prevNodeMap[server_id]
        prev.next = prev.next.next
        if prev.next is None:
            self.tail = prev
        else:
            self.prevNodeMap[prev.next.val] = prev

        del self.prevNodeMap[server_id]
        self.count -= 1


    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        if self.count == 0:
            return None

        steps = random.randint(0, self.count - 1)
        pt = self.head
        for _ in range(steps):
            pt = pt.next

        return pt.next.val