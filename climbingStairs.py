class Solution:
    def climbStairs(self, n: int) -> int:
        # best way to climb to nth step is to take the sum of n-1 and n-2 and determine if the last step
        # should be 1 or 2 steps

        # recursive solution
        # base case 1 and 2
        # top down DP
        memo = (n+1) * [-1]

        def climbStairsDP(n: int, memo: []):
            if memo[n] is not -1:
                return memo[n]
            if n == 1:
                memo[n] = 1
            elif n == 2:
                memo[n] = 2
            else:
                memo[n] = climbStairsDP(n - 1, memo) + \
                    climbStairsDP(n - 2, memo)

            return memo[n]

        return climbStairsDP(n, memo)
