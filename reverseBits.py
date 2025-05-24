class Solution:
    def reverseBits(self, n):
        ret, power = 0, 31
        print(4 & 1)
        while n:
            # bitwise comparison with 000000001 -> we only take the last 1 digit
            # we multiply that digit by the corresponding power and reversed (1s place become the largest)
            ret += (n & 1) << power
            # we divide n by 2 to move it to the next binary digit
            n = n >> 1
            # shif the power
            power -= 1
        return ret
