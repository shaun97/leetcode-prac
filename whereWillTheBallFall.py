class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        numOfBalls = len(grid[0])
        endLevel = len(grid)
        res = [-1] * numOfBalls

        for col in range(numOfBalls):
            currCol = col
            currLevel = 0

            while currLevel < endLevel:
                if grid[currLevel][currCol] == 1:
                    if currCol + 1 == numOfBalls or grid[currLevel][currCol + 1] == -1:
                        break
                    currCol += 1
                else:
                    if currCol - 1 == -1 or grid[currLevel][currCol - 1] == 1:
                        break
                    currCol -= 1

                currLevel += 1
            if currLevel == endLevel:
                res[col] = currCol

        return res
