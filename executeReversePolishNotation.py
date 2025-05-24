class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for token in tokens:
            if token == "+":
                first = stack.pop()
                second = stack.pop()
                res = first + second
                stack.append(res)
            elif token == "-":
                first = stack.pop()
                second = stack.pop()
                res = second - first
                stack.append(res)
            elif token == "*":
                first = stack.pop()
                second = stack.pop()
                res = first * second
                stack.append(res)
            elif token == "/":
                first = stack.pop()
                second = stack.pop()
                res = int(second / first)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack.pop()


def evalRPNLambda(self, tokens: List[str]) -> int:

    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: int(a / b),
        "*": lambda a, b: a * b
    }

    stack = []
    for token in tokens:
        if token in operations:
            number_2 = stack.pop()
            number_1 = stack.pop()
            operation = operations[token]
            stack.append(operation(number_1, number_2))
        else:
            stack.append(int(token))
    return stack.pop()
