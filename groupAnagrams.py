class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            sortedStr = "".join(sorted(string))
            if anagrams.get(sortedStr):
                anagrams[sortedStr].append(string)
            else:
                anagrams[sortedStr] = [string]

        res = []
        for key, item in anagrams.items():
            res.append(item)
        return res
