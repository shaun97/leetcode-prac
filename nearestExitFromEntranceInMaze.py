class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # BFS to find the exit 
        q = deque()
        q.append(entrance)
        q.append([-1, -1])
        end_row, end_col = len(maze), len(maze[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        no_of_steps = 0
        visited = set()
        while q:
            cell_x, cell_y = q.popleft()
            # check if it is an exit
            if cell_x == -1:
                no_of_steps += 1
                q.append([-1, -1])
                cell_x, cell_y = q.popleft()
            if (cell_x, cell_y) in visited:
                continue
            visited.add((cell_x, cell_y))

            if (cell_x == 0 or cell_x == end_row - 1 or cell_y == 0 or cell_y == end_col - 1) and (cell_x != entrance[0] or cell_y != entrance[1]):
                return no_of_steps
            else:
                for direction in directions:
                    new_x, new_y = cell_x + direction[0], cell_y + direction[1]
                    if new_x == -1 or new_x == end_row or new_y == -1 or new_y == end_col:
                        continue
                    if maze[new_x][new_y] != "+":
                        q.append([new_x, new_y])
        return -1