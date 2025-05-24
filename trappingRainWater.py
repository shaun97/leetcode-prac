class Solution:
    def trapStacks(self, height: List[int]) -> int:
        q = deque()
        amtOfWater = 0

        for i in range(0, len(height)):
            curr = height[i]
            while len(q) and curr > height[q[0]]:
                top = q.popleft()
                if len(q) == 0:
                    break
                distance = i - 1 - q[0]
                boundedHeight = min(curr, height[q[0]]) - height[top]
                amtOfWater += (distance * boundedHeight)

            q.appendleft(i)

        return amtOfWater

    def trapDP(self, height: List[int]) -> int:
        n = len(height)
        amtOfWater = 0

        leftArray = [-1] * n
        leftArray[0] = height[0]
        rightArray = [-1] * n
        rightArray[n - 1] = height[n - 1]

        # setup dp tables
        for i in range(1, n):
            leftArray[i] = max(leftArray[i - 1], height[i])

        for i in range(n - 2, -1, -1):
            rightArray[i] = max(rightArray[i + 1], height[i])

        for i in range(0, n):
            amtOfWater += min(leftArray[i], rightArray[i]) - height[i]

        return amtOfWater
