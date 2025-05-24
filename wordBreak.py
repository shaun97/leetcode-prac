class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # add word dict into a dict
        # backtracking to explore the different words? DP

        wordSet = frozenset(wordDict)

        @lru_cache
        def backtrack(string):

            if string in wordSet:
                return True

            currString = ""

            for idx, char in enumerate(string):
                currString += char
                if currString in wordSet:
                    if backtrack(string[idx + 1:]):
                        return True
            return False

        return backtrack(s)
