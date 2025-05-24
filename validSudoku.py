class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we'll use 27 sets to represent all the checks
        # iterate throgh every cell and add it to the set. If it already exist, it is not valid. Return
        # 0 - 8 for rows, 9 - 17 for cols, 18 - 26 for squares
        check = [set() for _ in range(27)]

        for row in range(len(board)):
            for col in range(len(board[0])):
                value = board[row][col]
                if value == ".":
                    continue
                if value in check[row]:
                    return False
                check[row].add(value)

                if value in check[col + 9]:
                    return False
                check[col + 9].add(value)

                square = (row // 3 * 3) + col // 3
                if value in check[square + 18]:
                    return False
                check[square + 18].add(value)

        return True
