class Solution:
    def countTime(self, time: str) -> int:
        res = 1

        for idx, number in enumerate(time):
            if number == ":":
                continue
            if number == "?":
                if idx == 4:
                    res *= 10
                elif idx == 3:
                    res *= 6
                elif idx == 1:
                    if time[idx - 1] == "?":
                        res *= 24
                    elif time[idx - 1] == "2":
                        res *= 4
                    else:
                        res *= 10
            elif idx == 1 and time[idx - 1] == "?":
                if int(number) < 4:
                    res *= 3
                else:
                    res *= 2

        return res
