class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        if not self.min or val <= self.min[-1]:
            self.min.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.min[-1] == self.stack.pop():
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
