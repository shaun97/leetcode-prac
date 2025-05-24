class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortestString = len(strs[0])

        for string in strs:
            if len(string) < shortestString:
                shortestString = len(string)
        res = ""
        for i in range(shortestString):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    return res
            res += char

        return res
