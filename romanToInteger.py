class Solution:
    def intToRoman(self, num: int) -> str:
        mappings = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        res = ""
        for value, letter in mappings.items():
            while value <= num:
                res += letter
                num -= value
        return res
