class StackNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Stack:

    head = StackNode()  #dummy node

    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        self.head.next = StackNode(x, self.head.next)

    """
    @return: nothing
    """
    def pop(self):
        if self.isEmpty():
            return

        self.head.next = self.head.next.next

    """
    @return: An integer
    """
    def top(self):
        if self.isEmpty():
            return

        return self.head.next.val

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return self.head.next is None