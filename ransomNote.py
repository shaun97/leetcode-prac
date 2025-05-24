import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Naive solution would be to iterate through ransomeNote and for each character, go through magazine and remove it from magazine if found
        # o(n2) solution

        # Loop through magazine and store all the characters using a dictionary and the number of times it appears
        # Loop through ransomNote to find if characters inside can be found in the dict
        # Check for obvious fail case.
        if len(ransomNote) > len(magazine):
            return False
        mDict = collections.Counter(magazine)

        for j in ransomNote:
            if mDict[j] <= 0:
                return False
            mDict[j] -= 1
        return True
