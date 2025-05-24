class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))
        startingPlace = len(res) - 1
        carry = 0
        for i in range(len(num1) - 1, -1, -1):
            currPlace = startingPlace
            for j in range(len(num2) - 1, -1, -1):
                currValue = int(num1[i]) * int(num2[j]) + carry
                res[currPlace] += currValue % 10
                res[currPlace - 1] += res[currPlace] // 10
                res[currPlace] = res[currPlace] % 10
                carry = currValue // 10
                currPlace -= 1

            if carry > 0:
                res[currPlace] += carry
                carry = 0

            startingPlace -= 1

        for idx, i in enumerate(res):
            if i != 0:
                return "".join(str(i) for i in res[idx:])
        return "0"
