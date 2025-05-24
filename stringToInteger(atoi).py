class Solution:
    def myAtoi(self, s: str) -> int:
        maxVal = 2 ** 31 - 1
        minVal = - 2 ** 31

        res = 0
        power = 10
        noOfPlaces = 0
        isNegative = False
        limit = 214748364
        isNumber = False

        for i in range(len(s)):
            if ord(s[i]) < 48 or ord(s[i]) > 57:
                if isNumber:
                    break
                if s[i] == " ":
                    continue
                elif s[i] == "-":
                    isNumber = True
                    isNegative = True
                elif s[i] == "+":
                    isNumber = True
                else:
                    break
            else:
                isNumber = True
                if res == 0 and int(s[i]) == 0:
                    continue
                noOfPlaces += 1
                res = res * power + int(s[i])

            if noOfPlaces == 9:

                if res < limit:
                    if len(s) - 1 == i:
                        continue
                    elif isNegative:
                        if (57 >= ord(s[i + 1]) >= 48) and ((i+2) < len(s) and 57 >= ord(s[i + 2]) >= 48):
                            return minVal
                    else:
                        if (57 >= ord(s[i + 1]) >= 48) and ((i+2) < len(s) and 57 >= ord(s[i + 2]) >= 48):
                            return maxVal
                elif res == limit:
                    if len(s) - 1 == i:
                        continue
                    elif isNegative:
                        if int(s[i + 1]) > 8 or ((i+2) < len(s) and 57 >= ord(s[i + 2]) >= 48):
                            return minVal
                    else:
                        if int(s[i + 1]) > 7 or ((i+2) < len(s) and 57 >= ord(s[i + 2]) >= 48):
                            return maxVal
                elif res > limit:
                    if isNegative:
                        # if int(s[i + 1]) > 8 or ((i+2) < len(s) and 57 >= ord(s[i + 2]) >= 48):
                        return minVal
                    else:
                        # if int(s[i + 1]) > 7 or ((i+2) < len(s) and 57 >= ord(s[i + 2]) >= 48):
                        return maxVal

        if isNegative:
            res = -1 * res

        return res
