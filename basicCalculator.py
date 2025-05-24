class Solution:
    def calculate(self, s: str) -> int:
        stack = deque()
        operand = 0
        res = 0
        sign = 1

        for char in s:
            if char.isdigit():
                operand = (operand * 10) + int(char)
            elif char == "+":
                res += sign * operand
                sign = 1
                operand = 0
            elif char == "-":
                res += sign * operand
                sign = -1
                operand = 0
            elif char == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif char == ")":
                res += sign * operand

                # multiply it by the sign right before the bracket
                res *= stack.pop()
                res += stack.pop()

                operand = 0

        return res + sign * operand
