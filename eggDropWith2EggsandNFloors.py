class Solution:
    def twoEggDrop(self, n: int) -> int:
        # use the first egg to narrow down 
        counter = 1
        while n > 0:
            n -= counter
            counter += 1
        return counter - 1