class Trie:

    def __init__(self):
        self.isCompleteWord = False
        self.children = 26 * [None]

    def insert(self, word: str) -> None:
        currNode = self
        for idx, char in enumerate(word):
            position = ord(char) - 97
            if currNode.children[position] == None:
                currNode.children[position] = Trie()
            currNode = currNode.children[position]
        currNode.isCompleteWord = True

    def search(self, word: str) -> bool:
        currNode = self
        for idx, char in enumerate(word):
            position = ord(char) - 97
            if currNode.children[position] == None:
                return False
            currNode = currNode.children[position]
        return currNode.isCompleteWord

    def startsWith(self, prefix: str) -> bool:
        currNode = self
        for char in prefix:
            idx = ord(char) - 97
            if currNode.children[idx] == None:
                return False
            currNode = currNode.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
