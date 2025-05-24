class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search to find the row and then binary search within the row
        top, bottom = 0, len(matrix) - 1
        row = 0
        while top <= bottom:
            mid = top + (bottom - top) // 2

            if ((mid == len(matrix) - 1) and matrix[mid][0] <= target) or (target >= matrix[mid][0] and target < matrix[mid + 1][0]):

                row = mid
                break
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                top = mid + 1

        left, right = 0, len(matrix[0]) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
