class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # preprocess into dictionaries where the keys are "*og" etc, to signify that these are the words that are linked via 1 letter difference

        wordDict = {}
        for word in wordList:
            for index in range(len(word)):
                wildCardWord = word[:index] + "*" + word[index + 1:]
                if wordDict.get(wildCardWord):
                    wordDict[wildCardWord].append(word)
                else:
                    wordDict[wildCardWord] = [word]

        visited = set()
        # perform BFS to find the end word
        q = deque()
        q.append(beginWord)
        step = 1

        while True:
            newq = deque()
            while q:
                currWord = q.pop()
                if currWord in visited:
                    continue
                visited.add(currWord)
                if currWord == endWord:
                    return step
                for index in range(len(currWord)):
                    wildCardWord = currWord[:index] + \
                        "*" + currWord[index + 1:]
                    if wordDict.get(wildCardWord):
                        possibleWords = wordDict[wildCardWord]
                        for word in possibleWords:
                            newq.append(word)

            if len(newq) == 0:
                break
            q = newq
            step += 1

        return 0
