class ThreeStacks:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        self.size = size
        self.stacks =[[],[],[]]

    """
    @param: stackNum: An integer
    @param: value: An integer
    @return: nothing
    """
    def push(self, stackNum, value):
        self.stacks[stackNum].append(value)

    """
    @param: stackNum: An integer
    @return: the top element
    """
    def pop(self, stackNum):
        return self.stacks[stackNum].pop()

    """
    @param: stackNum: An integer
    @return: the top element
    """
    def peek(self, stackNum):
        return self.stacks[stackNum][-1]

    """
    @param: stackNum: An integer
    @return: true if the stack is empty else false
    """
    def isEmpty(self, stackNum):
        return len(self.stacks[stackNum]) == 0