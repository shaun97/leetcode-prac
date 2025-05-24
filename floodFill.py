from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        visited = set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        if image[sr][sc] == color:
            return image
        rows, cols = len(image), len(image[0])
        q.append((sr, sc))
        start_color = image[sr][sc]

        image[sr][sc] = color

        while q:
            i, j = q.popleft()
            if (i, j) in visited:
                continue
            visited.add((i, j))
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]

                if 0 <= next_i < rows and 0 <= next_j < cols:
                    if image[next_i][next_j] == start_color:
                        q.append((next_i, next_j))
                        image[next_i][next_j] = color
        return image
