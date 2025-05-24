class Solution:
    def countSubstrings(self, s: str) -> int:
        # we iterate through all the letters and use each of them as 1) the centre 2) as the first element of
        # an even length substring and expand outwards, checking if they are a substring

        res = 0

        for idx in range(len(s)):
            start = idx
            end = idx

            while start > -1 and end < len(s):
                if s[start] == s[end]:
                    res += 1
                else:
                    break
                start -= 1
                end += 1

            if idx < len(s) - 1:
                start = idx
                end = idx + 1
                while start > -1 and end < len(s):
                    if s[start] == s[end]:
                        res += 1
                    else:
                        break

                    start -= 1
                    end += 1

        return res
