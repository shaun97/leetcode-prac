class Solution:
    # Times out but added some optimisation pre checks
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = set()
        maxRow = len(board)
        maxCol = len(board[0])

        # takes in the pt (tuple) and targetWord
        def backtrack(startPt, wordStartIndex):
            # print(board[startPt[0]][startPt[1]])
            if (len(word) - 1) == wordStartIndex:
                if board[startPt[0]][startPt[1]] == word[wordStartIndex]:
                    return True
                else:
                    return False
            if word[wordStartIndex] != board[startPt[0]][startPt[1]]:
                return False

            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            for direction in directions:
                newX = startPt[0] + direction[0]
                newY = startPt[1] + direction[1]
                newPt = (newX, newY)
                if newX > -1 and newX < maxRow and newY > -1 and newY < maxCol and newPt not in visited:
                    visited.add(newPt)
                    if backtrack(newPt, wordStartIndex + 1):
                        return True
                    else:
                        visited.remove(newPt)
            return False

        counter = {}
        for row in range(maxRow):
            for col in range(maxCol):
                if board[row][col] in counter:
                    counter[board[row][col]] += 1
                else:
                    counter[board[row][col]] = 1

        for char in word:
            if char not in counter:
                return False
            else:
                counter[char] -= 1
                if counter[char] < 0:
                    return False

        for row in range(maxRow):
            for col in range(maxCol):
                if board[row][col] != word[0]:
                    continue
                visited.add((row, col))
                if backtrack((row, col), 0):
                    return True
                visited.remove((row, col))
        return False
