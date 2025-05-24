class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(s, start, end):
            while 0 <= start and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1

            return s[start + 1: end]

        res = ""
        for i in range(len(s)):
            res = max(helper(s, i, i), helper(s, i, i + 1), res, key=len)

        return res
