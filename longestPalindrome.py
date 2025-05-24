class Solution:
    def longestPalindrome(self, s: str) -> int:
        # put all the char in a dict with their respective counts and only include those w even numbers
        book = {}
        for char in s:
            if char in book:
                book[char] += 1
            else:
                book[char] = 1

        longestStr = 0
        for key, no in book.items():
            if no % 2 == 0:
                longestStr += no
            else:
                longestStr += (no - 1)

        if len(s) > longestStr:
            longestStr += 1

        return longestStr
