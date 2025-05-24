class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""

        str_list = list(palindrome)
        str_len = len(str_list)

        for i in range(0, str_len // 2):
            if str_list[i] != "a":
                str_list[i] = "a"
                return "".join(str_list)
        str_list[str_len - 1] = "b"
        return "".join(str_list)