from queue import PriorityQueue


class MedianFinder:

    def __init__(self):
        self.leftHalf = PriorityQueue()  # p queue with max heap
        self.rightHalf = PriorityQueue()  # p queue with min heap

    def addNum(self, num: int) -> None:

        if self.rightHalf.qsize() > 0 and num > self.rightHalf.queue[0]:
            self.rightHalf.put(num)
        else:
            self.leftHalf.put(-num)

        if self.rightHalf.qsize() - self.leftHalf.qsize() > 1:
            self.leftHalf.put(-self.rightHalf.get())
        elif self.leftHalf.qsize() - self.rightHalf.qsize() > 1:
            self.rightHalf.put(-self.leftHalf.get())

    def findMedian(self) -> float:
        if self.rightHalf.qsize() == self.leftHalf.qsize():
            return (self.rightHalf.queue[0] + (-self.leftHalf.queue[0])) / 2
        elif self.rightHalf.qsize() > self.leftHalf.qsize():
            return self.rightHalf.queue[0]
        else:
            return (-self.leftHalf.queue[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
