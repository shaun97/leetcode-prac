class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]

        def memo_solve(start1, start2, text1, text2, dp):
            if start1 == len(text1) or start2 == len(text2):
                return 0

            if dp[start1][start2] != -1:
                return dp[start1][start2]

            # if the start letter are the same
            if text1[start1] == text2[start2]:
                dp[start1][start2] = 1 + \
                    memo_solve(start1 + 1, start2 + 1, text1, text2, dp)
            else:
                dp[start1][start2] = max(memo_solve(
                    start1 + 1, start2, text1, text2, dp), memo_solve(start1, start2 + 1, text1, text2, dp))

            return dp[start1][start2]

        return memo_solve(0, 0, text1, text2, dp)
