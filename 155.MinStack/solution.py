class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if self.min is None:
            self.min = val
        else:
            self.min = min(self.min, val)
        self.stack.append(val)

    def pop(self) -> None:
        poppedItem = self.stack.pop()
        if self.min == poppedItem:
            self.min = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
