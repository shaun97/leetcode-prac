from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # loop through the entire grid, if we hit land, we do BFS and mark as visited
        # change land to 2 if visited
        rows, cols = len(grid), len(grid[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        no_of_islands = 0

        for r in range(rows):
            for c in range(cols):
                # check if land
                if grid[r][c] == "1":
                    q = deque([(r, c)])

                    while q:
                        curr_r, curr_c = q.popleft()
                        if grid[curr_r][curr_c] == "1":
                            grid[curr_r][curr_c] = "2"
                            for direction in directions:
                                next_r, next_c = curr_r + \
                                    direction[0], curr_c + direction[1]
                                if 0 <= next_r < rows and 0 <= next_c < cols:
                                    q.append((next_r, next_c))
                    no_of_islands += 1
        return no_of_islands
