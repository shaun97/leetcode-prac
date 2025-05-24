class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for i in range(1, n):
            newRes = ""
            j = 0
            while j < len(res):
                freq = 0
                currNum = res[j]
                while j < len(res) and currNum == res[j]:
                    freq += 1
                    j += 1
                newRes += (str(freq) + currNum)
            res = newRes
        return res
