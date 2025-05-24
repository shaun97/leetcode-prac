class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = (amount + 1) * [math.inf]
        memo[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                memo[x] = min(memo[x], memo[x - coin] + 1)

        if memo[amount] == math.inf:
            return -1

        return memo[amount]
