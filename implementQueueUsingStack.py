from collections import deque


class MyQueue:

    def __init__(self):
        # using only pop pop and append which access elements from the right like a stack
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        # If it is empty, ill transfer all the items from stack 1 to 2
        if len(self.stack2) == 0:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self) -> int:
        # If it is empty, ill transfer all the items from stack 1 to 2
        if len(self.stack2) == 0:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())

        ret = self.stack2.pop()
        self.stack2.append(ret)
        return ret

    def empty(self) -> bool:
        if (len(self.stack1) + len(self.stack2) == 0):
            return True
        else:
            return False
