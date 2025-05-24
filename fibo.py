class Solution:
    def fib(self, n: int) -> int:
        memo = (n + 1) * [-1]

        def fibDP(n, memo):
            if memo[n] == -1:
                if n == 0:
                    memo[n] = 0
                elif n == 1:
                    memo[n] = 1
                else:
                    memo[n] = fibDP(n-1, memo) + fibDP(n-2, memo)

            return memo[n]

        return fibDP(n, memo)
