from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if len(stack) != 0:
                    open_bracket = stack.pop()
                else:
                    return False

                if (open_bracket == '(' and char != ')') or (open_bracket == '{' and char != '}') or (open_bracket == '[' and char != ']'):
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
