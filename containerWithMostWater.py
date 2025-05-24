class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        maxArea = 0

        while start < end:
            tankHeight = min(height[start], height[end])
            tankWidth = end - start
            tankArea = tankHeight * tankWidth

            maxArea = max(maxArea, tankArea)

            if height[start] > height[end]:
                end -= 1
            else:
                start += 1

        return maxArea
