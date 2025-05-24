class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numberArray = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], [
            "m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]

        res = []
        for digit in digits:
            digit = int(digit)
            if len(res) == 0:
                res = numberArray[digit - 2]
            else:
                res = [combi + char for char in numberArray[digit - 2]
                       for combi in res]
        return res
