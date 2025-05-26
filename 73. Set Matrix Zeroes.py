# 73. Set Matrix Zeroes
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        fColFlag = 1
        fRowFlag = 1
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                fColFlag = 0
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                fRowFlag = 0
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] == 0:
                    matrix[0][x] = 0
                    matrix[y][0] = 0
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        if fColFlag == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if fRowFlag == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
