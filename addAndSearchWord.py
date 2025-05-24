class TrieNode:
    def __init__(self, char, isComplete):
        self.children = {}
        self.char = char
        self.isComplete = isComplete


class WordDictionary:

    def __init__(self):
        self.root = TrieNode("-", False)
        self.maxWordLen = 0

    def addWord(self, word: str) -> None:
        if len(word) > self.maxWordLen:
            self.maxWordLen = len(word)
        curr = self.root
        for char in word:
            if not curr.children.get(char):
                curr.children[char] = TrieNode(char, False)
            curr = curr.children[char]
        curr.isComplete = True

    def search(self, word: str) -> bool:
        if len(word) > self.maxWordLen:
            return False

        def searchRecursive(index, word, node):
            curr = node
            char = word[index]

            if char == ".":
                if index == len(word) - 1:
                    for key, item in curr.children.items():
                        if item.isComplete:
                            return True
                    return False
                else:
                    for key, item in curr.children.items():
                        if searchRecursive(index + 1, word, item):
                            return True
                    return False
            else:
                if index == len(word) - 1:
                    if curr.children.get(char) and curr.children[char].isComplete:
                        return True
                    else:
                        return False
                else:
                    if not curr.children.get(char):
                        return False
                    else:
                        return searchRecursive(index + 1, word, curr.children[char])

        return searchRecursive(0, word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
