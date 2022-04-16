class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.frontStack = []
        self.backStack = []
        self.front = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.frontStack:
            self.front = x
        self.frontStack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.backStack:
            while self.frontStack:
                self.backStack.append(self.frontStack.pop())
        return self.backStack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.backStack:
            return self.backStack[-1]
        else:
            return self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.frontStack and not self.backStack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
