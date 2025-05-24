class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        isNegative = False

        max = 2 ** 31

        power = 0

        if x < 0:
            isNegative = True
            x *= -1

        while x:
            digit = x % 10
            x //= 10
            res *= 10
            res += digit
            power += 1
            if power == 9:
                if (res > 214748364 and x > 0) or (res == 214748364 and x > 7 and not isNegative) or (res == 214748364 and x > 8 and isNegative):
                    return 0

        return res * -1 if isNegative else res
