class Solution:
    def numDecodings(self, s: str) -> int:
        # Where the ith place is the number of ways to decode from the start of the string to the ith char
        dp = [0] * len(s)

        def decodeWays(start, s, dp):
            if s[start] == "0":
                return 0

            if dp[start] > 0:
                return dp[start]

            if start == len(s) - 1:
                dp[start] = 1
                return 1
            elif start == len(s) - 2 and int(s[start:start + 2]) < 27:
                if s[start + 1] == "0":
                    dp[start] = 1
                else:
                    dp[start] = 2
                return dp[start]

            ways = 0
            if start < len(s) - 1:
                if int(s[start:start + 2]) < 27:
                    ways += decodeWays(start + 2, s, dp)

            ways += decodeWays(start + 1, s, dp)

            dp[start] = ways
            return ways

        decodeWays(0, s, dp)

        return dp[0]
