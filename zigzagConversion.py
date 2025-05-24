class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < numRows or numRows == 1:
            return s

        rowStrings = [""] * numRows

        isFlat = False
        row = 0

        for idx, char in enumerate(s):
            rowStrings[row] += char

            if isFlat:
                if row == (numRows - 1):
                    isFlat = False
                    row -= 1
                else:
                    row += 1
            else:
                if row == 0:
                    isFlat = True
                    row += 1
                else:
                    row -= 1

        res = ''

        for string in rowStrings:
            res += string

        return ''.join(res)
