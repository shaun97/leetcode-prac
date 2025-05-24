class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        plength = len(p)

        start = 0
        end = plength - 1

        pdict = Counter(p)
        currdict = Counter(s[start:end + 1])

        while end < len(s):
            if currdict == pdict:
                res.append(start)

            start += 1
            end += 1

            currdict[s[start - 1]] -= 1
            if currdict[s[start - 1]] == 0:
                del currdict[s[start - 1]]

            if end < len(s):
                print(s[end])
                if s[end] in currdict:
                    currdict[s[end]] += 1
                else:
                    currdict[s[end]] = 1

        return res
