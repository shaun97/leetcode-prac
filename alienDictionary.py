from collections import deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Initialise the adj list of all letters
        adjList = {}
        inDegree = {}
        for word in words:
            for char in word:
                adjList[char] = set()
                inDegree[char] = 0

        # get the rules, can this be words[:-1]? Doesn't matter -> itll only run until n - times
        for firstWord, secondWord in zip(words, words[1:]):
            isPrefix = True
            for firstWordLetter, secondWordLetter in zip(firstWord, secondWord):
                if firstWordLetter != secondWordLetter:
                    if secondWordLetter not in adjList[firstWordLetter]:
                        adjList[firstWordLetter].add(secondWordLetter)
                        inDegree[secondWordLetter] += 1
                    isPrefix = False
                    break
            if isPrefix:
                if len(secondWord) < len(firstWord):
                    return ""

        # topological sort - BFS
        q = deque()
        output = []

        for node, inDeg in inDegree.items():
            if inDeg == 0:
                q.append(node)
        while q:
            node = q.popleft()
            output.append(node)

            for neighbour in adjList[node]:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    q.append(neighbour)

        if len(output) < len(inDegree):
            return ""

        return "".join(output)
