class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)

        def recurse(idx, lastChar, count, k):
            if (idx, lastChar, count, k) in dp:
                return dp[(idx, lastChar, count, k)]

            if k < 0:
                return math.inf
            elif idx == n:
                return 0

            # last char is the same -> we check the compression length if we add
            # we decide if we wanna minus k or not which affect the compression length
            if lastChar == s[idx]:
                carry = 0
                if count == 99 or count == 9 or count == 999 or count == 1:
                    carry += 1
                # we delete s[idx] vs we dont delete
                res = min(recurse(idx + 1, lastChar, count, k - 1),
                          recurse(idx + 1, s[idx], count + 1, k) + carry)
                dp[(idx, lastChar, count, k)] = res

            else:
                res = min(recurse(idx + 1, lastChar, count, k - 1),
                          recurse(idx + 1, s[idx], 1, k) + 1)
                dp[(idx, lastChar, count, k)] = res

            return dp[(idx, lastChar, count, k)]

        dp = {}
        return int(recurse(0, ' ', 0, k))
