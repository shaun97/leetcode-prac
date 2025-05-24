class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # isChange -> signifies there was a chnage in the prev minute
        # let i be the minute (max would be len(grid) * len(grid))
        # we return if there has not been a change

        # we can prune by checking if there is an orange that is not bounded by any adjacent orange?
        changes = []
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        isChange = True

        minute = 0
        while isChange:
            isChange = False
            isFreshLeft = False
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    isRotten = False
                    if grid[row][col] == 2 or grid[row][col] == 0:  # rotten or empty
                        continue

                    for direction in directions:
                        if row + direction[0] > -1 and row + direction[0] < len(grid) and col + direction[1] > -1 and col + direction[1] < len(grid[0]):
                            if grid[row + direction[0]][col + direction[1]] == 2:
                                changes.append([row, col])
                                break

            for change in changes:
                grid[change[0]][change[1]] = 2
                isChange = True

            if isChange:
                minute += 1

            changes = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1

        return minute

    def orangesRottingBFS(self, grid: List[List[int]]) -> int:
        # Look for all rotting oranges and add them to the queue
        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append([row, col])

        q.append([-1, -1])
        minute = -1

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while q:
            curr = q.popleft()
            row = curr[0]
            col = curr[1]
            if row == -1:
                q.append([-1, -1])
                minute += 1
                if len(q) == 1:
                    break
                curr = q.popleft()
                row = curr[0]
                col = curr[1]
            for direction in directions:
                next_row, next_col = row + direction[0], col + direction[1]

                if next_row > -1 and next_row < rows and next_col > -1 and next_col < cols:
                    print(next_row, next_col, grid[next_row][next_col])
                    if grid[next_row][next_col] == 1:
                        grid[next_row][next_col] = 2
                        q.append([next_row, next_col])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        return minute
