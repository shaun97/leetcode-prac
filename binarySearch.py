class Solution:
    # O(log N) space
    def searchRecurse(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        def binary_search(nums, left, right, target) -> int:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if (left >= right):
                return -1

            if nums[mid] > target:
                return binary_search(nums, left, mid - 1, target)
            else:
                return binary_search(nums, mid + 1, right, target)

        return binary_search(nums, left, right, target)

    # O(1) space
    def searchIterative(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1