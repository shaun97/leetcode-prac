class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = [0] * 26
        count = 0
        for char in sentence:
            if(letters[ord(char) - 97]) == 0:
                letters[ord(char) - 97] = 1
                count += 1
                if count == 26:
                    return True
        return False
