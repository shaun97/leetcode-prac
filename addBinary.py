class Solution:
    def addBinaryBitManipulation(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)
        carry = 0
        ans = deque()

        for i in range(n - 1, -1, -1):
            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry += 1

            if carry == 3:
                carry = 1
                ans.appendleft("1")
            elif carry == 2:
                carry = 1
                ans.appendleft("0")
            elif carry == 1:
                carry = 0
                ans.appendleft("1")
            else:
                carry = 0
                ans.appendleft("0")

        if carry == 1:
            ans.appendleft("1")
        print(ans)

        return "".join(ans)

    def addBinaryFunctions(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        return format(a + b, "b")

    def addBinaryBit(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        return format(a + b, "b")
