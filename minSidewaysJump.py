class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        # DP[i] represents the min number of jumps to reach this spot from start until iteration k
        dp = [1, 0, 1]
        for k in obstacles:
            if k != 0:
                dp[k - 1] = math.inf
            for i in range(3):
                if (i + 1) != k:  # Frogs can only side jump if the same point has no obstacle in that lane
                    dp[i] = min(dp[i], dp[(i + 1) % 3] +
                                1, dp[(i + 2) % 3] + 1)

        return min(dp)

        # 1 0 1 -> 2
        # 1 inf 1 -> 1
        # inf 2 1 -> 3
        # 3 2 inf

