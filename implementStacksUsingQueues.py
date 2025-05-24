from queue import Queue


class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q1.put(x)

    def pop(self) -> int:
        while self.q1.qsize() > 1:
            temp = self.q1.get()
            self.q2.put(temp)

        ret = self.q1.get()

        while not self.q2.empty():
            temp = self.q2.get()
            self.q1.put(temp)

        return ret

    def top(self) -> int:
        while self.q1.qsize() > 1:
            temp = self.q1.get()
            self.q2.put(temp)

        ret = self.q1.get()
        self.q2.put(ret)

        while not self.q2.empty():
            temp = self.q2.get()
            self.q1.put(temp)

        return ret

    def empty(self) -> bool:
        return self.q1.empty()


class MyStack1Queue:

    def __init__(self):
        self.q1 = Queue()

    def push(self, x: int) -> None:
        size = self.q1.qsize()
        self.q1.put(x)
        for i in range(size):
            self.q1.put(self.q1.get())

    def pop(self) -> int:
        return self.q1.get()

    def top(self) -> int:
        temp = self.q1.get()
        self.push(temp)
        return temp

    def empty(self) -> bool:
        return self.q1.empty()
