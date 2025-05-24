class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        dist = [[math.inf for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    continue
                top_and_left = ((-1, 0), (0, -1))

                for direction in top_and_left:
                    prev_i, prev_j = i + direction[0], j + direction[1]
                    if 0 <= prev_i < rows and 0 <= prev_j < cols:
                        dist[i][j] = min(dist[prev_i][prev_j] + 1, dist[i][j])

        for i in reversed(range(rows)):
            for j in reversed(range(cols)):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    continue
                bot_and_right = ((1, 0), (0, 1))

                for direction in bot_and_right:
                    prev_i, prev_j = i + direction[0], j + direction[1]
                    if 0 <= prev_i < rows and 0 <= prev_j < cols:
                        dist[i][j] = min(dist[prev_i][prev_j] + 1, dist[i][j])

        return dist
