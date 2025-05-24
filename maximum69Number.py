class Solution:
    def maximum69Number (self, num: int) -> int:
        lengthOfNum = 0
        temp = num
        while temp:
            temp //= 10
            lengthOfNum += 1

        while lengthOfNum:
            digit = num % (10 ** (lengthOfNum))
            digit = digit // (10 ** (lengthOfNum - 1))

            if digit == 6:
                num -= digit * (10 ** (lengthOfNum - 1))
                num += 9 * (10 ** (lengthOfNum - 1))
                return num

            lengthOfNum -= 1
        return num