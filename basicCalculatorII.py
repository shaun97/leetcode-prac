class Solution:
    def calculate(self, s: str) -> int:
        s = "".join(s.split(" "))
        q = deque()
        idx = 0
        curr = 0
        while idx < len(s):
            if s[idx] != "*" and s[idx] != "/" and s[idx] != "+" and s[idx] != "-":
                curr *= 10
                curr += int(s[idx])
            else:
                q.append(curr)
                curr = 0
                q.append(s[idx])
            idx += 1
        q.append(curr)

        new_q = deque()
        prev = 0
        while q:
            curr = q.popleft()
            if curr == "*":
                prev = q.popleft() * prev
            elif curr == "/":
                prev //= q.popleft()
            elif curr == "+":
                new_q.append(prev)
                new_q.append("+")
            elif curr == "-":
                new_q.append(prev)
                new_q.append("-")
            else:
                prev = curr
        new_q.append(prev)
        res = 0
        print(list(new_q))
        while new_q:
            curr = new_q.popleft()
            if curr == "-":
                res -= new_q.popleft()
            elif curr == "+":
                res += new_q.popleft()
            else:
                res = curr

        return res

