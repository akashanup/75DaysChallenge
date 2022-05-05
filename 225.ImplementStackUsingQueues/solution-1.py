class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.topElement = None

    # O(1)
    def push(self, x: int) -> None:
        self.q1.append(x)
        self.topElement = x

    # O(n)
    def pop(self) -> int:
        while len(self.q1) > 1:
            self.topElement = self.q1.popleft()
            self.q2.append(self.topElement)
        topElement = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return topElement

    # O(1)
    def top(self) -> int:
        return self.topElement

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
