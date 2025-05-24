class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # backtracking with memoization

        dp = [[-1] * n for _ in range(m)]

        dp[m - 1][n - 1] = 0
        dp[m - 1][n - 2] = 1
        dp[m - 2][n - 1] = 1

        # returns the number of uniq paths
        def backtrack(startR, startC) -> int:
            if startR >= m or startC >= n:
                return 0

            if dp[startR][startC] == -1:
                down = backtrack(startR + 1, startC)
                right = backtrack(startR, startC + 1)
                dp[startR][startC] = down + right
                return down + right
            else:
                return dp[startR][startC]

        return backtrack(0, 0)

    def uniquePathsBottomUp(self, m: int, n: int) -> int:
        # backtracking with memoization

        dp = [[1] * n for _ in range(m)]

        for col in range(1, m):
            for row in range(1, n):
                dp[col][row] = dp[col - 1][row] + dp[col][row - 1]

        return dp[m - 1][n - 1]

    def uniquePaths1DArray(self, m: int, n: int) -> int:
        # backtracking with memoization

        dp = [1] * n
        # dp = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                dp[col] = dp[col - 1] + dp[col]
                # dp[row][col] = dp[row][col] + dp[row][col - 1]

        return dp[n - 1]
