class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # pointer to iterate through
        # binary search on the remaining values to find the complement
        res = []
        for i in range(len(numbers) - 1):
            num = numbers[i]
            comp = target - num
            left = i + 1
            right = len(numbers) - 1
            mid = left + (right - left) // 2
            while right >= left:
                if comp == numbers[mid]:
                    res = [i + 1, mid + 1]
                    break
                elif comp > numbers[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                mid = left + (right - left) // 2

        return res

    def twoSumTwoPointers(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        for _ in range(len(numbers)):
            if numbers[left] + numbers[right] == target:
                break
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

        return [left + 1, right + 1]
