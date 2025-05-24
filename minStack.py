from Queue import deque


class MinStack:

    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()
        self.s2.append(math.inf)

    def push(self, val: int) -> None:
        self.s1.append(val)
        if val <= self.s2[-1]:
            self.s2.append(val)

    def pop(self) -> None:
        val = self.s1.pop()
        if val == self.s2[-1]:
            self.s2.pop()

    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        return self.s2[-1]


class MinStackImproved:

    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()
        self.s2.append([math.inf, 1])

    def push(self, val: int) -> None:
        self.s1.append(val)
        if val == self.s2[-1][0]:
            self.s2[-1][1] += 1
        elif val < self.s2[-1][0]:
            self.s2.append([val, 1])

    def pop(self) -> None:
        val = self.s1.pop()
        if val == self.s2[-1][0]:
            self.s2[-1][1] -= 1
        if self.s2[-1][1] == 0:
            self.s2.pop()

    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        return self.s2[-1][0]
