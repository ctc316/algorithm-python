class MinStack:
    def __init__(self):
        self.minstack = []
        self.stack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        self.stack.append(number)
        if len(self.minstack) == 0 or number <= self.minstack[-1]:
            self.minstack.append(number)

    """
    @return: An integer
    """
    def pop(self):
        if self.minstack[-1] == self.stack[-1]:
            self.minstack.pop()
        return self.stack.pop()


    """
    @return: An integer
    """
    def min(self):
        return self.minstack[-1]