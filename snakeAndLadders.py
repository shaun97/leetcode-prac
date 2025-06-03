import heapq

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        boardMap = {}
        board.reverse()
        count = 1
        for i in range(0, len(board), 2):
            for j in range(len(board[0])):
                boardMap[count] = [i, j, board[i][j]]
                count += 1

            if i + 1 >= len(board):
                continue

            for j in range(len(board[0]) - 1, -1, -1):
                boardMap[count] = [i + 1, j, board[i+1][j]]
                count += 1
        count -= 1
        q = [] 
        heappush(q, [0, -1]) 
        visited = set()
        minMoves = 999999
        while q:
            moves, square = heappop(q)
            square = -square
            if square > count - 7:
                return moves + 1
            if square in visited:
                continue
            visited.add(square)
            for i in range(square + 1, square + 7, 1):
                if i >= count:
                    continue
                if boardMap[i][2] == -1:
                    heappush(q, [moves + 1,-i])
                else:
                    if boardMap[i][2] >= count:
                        return moves + 1
                    heappush(q, [moves + 1, -boardMap[i][2]])
        return -1
                    
        
