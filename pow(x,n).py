class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n  # floor division will cause this to be stuck at -1
        return self.fastPow(x, n)

    def fastPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n % 2 == 1:
            temp = self.fastPow(x, n // 2)
            return temp * temp * x
        else:
            temp = self.fastPow(x, n // 2)
            return temp * temp

    def fastPowIterative(self, x: float, n: int) -> float:
        ans = 1
        curr = x
        if (n == 0):
            return 1
        while n > 0:
            if n % 2 == 1:
                ans = curr * ans # Will always run on the last run as n = 1
            curr = curr * curr # this only squares the even values (odd numbers are dealt with separately)
            n = n // 2
        return ans
