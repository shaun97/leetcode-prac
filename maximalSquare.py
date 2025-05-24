class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [0] * (len(matrix[0]) + 1)
        maxRow = len(matrix)
        maxCol = len(matrix[0])
        prev = 0
        maxLen = 0

        for row in range(maxRow):
            for col in range(maxCol):
                temp = dp[col + 1]
                if matrix[row][col] == "1":
                    dp[col + 1] = min(dp[col], dp[col + 1], prev) + 1
                    maxLen = max(maxLen, dp[col + 1])
                else:
                    dp[col + 1] = 0
                prev = temp

        return maxLen ** 2