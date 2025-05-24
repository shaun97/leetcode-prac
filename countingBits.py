class Solution:
    def countBits(self, n: int) -> List[int]:
        count = [0] * (n + 1)
        x = 0
        b = 1

        # b is the index and x is the series that exist << 1 before b
        while b <= n:
            # generate [b, 2b) or [b, n) from [0, b) -> x represents the counter from 0
            while x < b and x + b <= n:
                count[x + b] = count[x] + 1
                x += 1
            x = 0
            b <<= 1

        return count

    def countBitsLSB(self, n: int) -> List[int]:
        count = [0] * (n + 1)
        x = 0
        b = 1

        # b is the index and x is the series that exist << 1 before b
        while b <= n:
            # generate [b, 2b) or [b, n) from [0, b) -> x represents the counter from 0
            while x < b and x + b <= n:
                count[x + b] = count[x] + 1
                x += 1
            x = 0
            b <<= 1

        return count
