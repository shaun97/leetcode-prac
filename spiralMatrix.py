class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # use a marker to marked visited cells
        # use numbers to iterate through
        # boolean to determine if we traversing vert or horizontal

        # while loop to control the boundaries
        res = []
        row_t = col_l = 0
        row_b = len(matrix) - 1
        col_r = len(matrix[0]) - 1
        is_horizontal = True
        is_forward = True

        while row_t <= row_b and col_l <= col_r:
            # We traverse horizontally
            if is_horizontal:
                if is_forward:
                    for i in range(col_l, col_r + 1):
                        res.append(matrix[row_t][i])
                    row_t += 1
                else:
                    for i in reversed(range(col_l, col_r + 1)):
                        res.append(matrix[row_b][i])
                    row_b -= 1
                is_horizontal = False
            else:
                if is_forward:
                    for i in range(row_t, row_b + 1):
                        res.append(matrix[i][col_r])
                    col_r -= 1
                    is_forward = False
                else:
                    for i in reversed(range(row_t, row_b + 1)):
                        res.append(matrix[i][col_l])
                    col_l += 1
                    is_forward = True
                is_horizontal = True
        return res

    def spiralOrderCleaner(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])  # Initial possible number of steps
        direction = 1  # Start off going right
        i, j = 0, -1
        output = []
        while m*n > 0:
            for _ in range(n):  # move horizontally
                j += direction
                output.append(matrix[i][j])
            m -= 1
            for _ in range(m):  # move vertically
                i += direction
                output.append(matrix[i][j])
            n -= 1
            direction *= -1  # flip direction
        return output

    def spiralOrderNextTry(self, matrix: List[List[int]]) -> List[int]:
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        currPointer = [0, 0]
        direction = [0, 1]
        res = []

        if len(matrix) == 1 and len(matrix[0]) == 1:
            return [matrix[0][0]]

        while left <= right and top <= bottom:
            currX, currY = currPointer[0], currPointer[1]
            print(currX, currY)
            res.append(matrix[currX][currY])
            # Check if we need to change direction
            # we are at top and we hit the right
            if currX == top and currY == right and direction == [0, 1]:
                top += 1
                direction = [1, 0]
            elif currX == bottom and currY == right and direction == [1, 0]:
                right -= 1
                direction = [0, -1]
            elif currX == bottom and currY == left and direction == [0, -1]:
                bottom -= 1
                direction = [-1, 0]
            elif currX == top and currY == left and direction == [-1, 0]:
                left += 1
                direction = [0, 1]

            # go to the next step
            currPointer = [currX + direction[0], currY + direction[1]]

        return res
