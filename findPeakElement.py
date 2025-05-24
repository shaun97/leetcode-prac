class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if (mid - 1 == -1 or nums[mid - 1] < nums[mid]) and (mid + 1 == len(nums) or nums[mid + 1] < nums[mid]):
                return mid
            elif nums[mid - 1] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1


    def findPeakElementClean(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid + 1] < nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left
