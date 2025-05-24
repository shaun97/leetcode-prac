class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        curr = n
        while True:
            sumSquared = 0
            while curr:
                sumSquared += (curr % 10) ** 2
                curr //= 10
            if sumSquared == 1:
                return True
            elif sumSquared in visited:
                return False
            else:
                curr = sumSquared
                visited.add(sumSquared)
