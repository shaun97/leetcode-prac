class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers, one at the end one at the front
        # loop to half of the array
        # if left value or right value not an alphabet, increment or decrement respectively
        # if uppercase, change it to lower case
        # compare the elements, if different, return false, if same, increment and decrement left and right
        # if lhs>rhs, ret true

        # Edge case -> empty string
        # Edge case -> alphanumeric
        s = list(s)
        lhs = 0
        length = len(s)
        rhs = length - 1
        for i in range(length):
            if lhs >= rhs:
                return True
            # uppercase convert to lowercase
            if s[lhs] >= 'A' and s[lhs] <= 'Z':
                s[lhs] = chr(ord(s[lhs]) - ord('A') + ord('a'))
            # not ascii
            elif (s[lhs] < 'a' or s[lhs] > 'z') and (s[lhs] < "0" or s[lhs] > "9"):
                lhs += 1
                continue

            # uppercase convert to lowercase
            if s[rhs] >= 'A' and s[rhs] <= 'Z':
                s[rhs] = chr(ord(s[rhs]) - ord('A') + ord('a'))
            # not ascii
            elif (s[rhs] < 'a' or s[rhs] > 'z') and (s[rhs] < "0" or s[rhs] > "9"):
                rhs -= 1
                continue

            if s[lhs] == s[rhs]:
                lhs += 1
                rhs -= 1
                continue
            else:
                return False

    def isPalindromeSimpler(self, s: str) -> bool:
        # two pointers, one at the end one at the front
        # loop to half of the array
        # if left value or right value not an alphabet, increment or decrement respectively
        # if uppercase, change it to lower case
        # compare the elements, if different, return false, if same, increment and decrement left and right
        # if lhs>rhs, ret true

        # Edge case -> empty string
        # Edge case -> alphanumeric
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
