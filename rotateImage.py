class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        # 0,0 -> 0,2 -> 2,2 -> 2,0
        # 0,1 -> 1,2 -> 2,1 -> 1,0
        # 0,2 -> 2,2 -> 2,0 -> 0,0

        # 1,1

        for i in range(0, n // 2 + 1):
            for j in range(i, n - i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - j][i]
                matrix[n - j][i] = matrix[n - i][n - j]
                matrix[n - i][n - j] = matrix[j][n - i]
                matrix[j][n - i] = temp
