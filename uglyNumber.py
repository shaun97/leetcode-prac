class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        primeToCheck = [2, 3, 5]

        for prime in primeToCheck:
            while n % prime == 0:
                n //= prime
        if n != 1:
            return False
        return True

        