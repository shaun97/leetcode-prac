class Solution:
    def searchRecur(self, nums: List[int], target: int) -> int:
        # It has to be O(logn) which means that we will have to use binary search
        # Modified binary search.
        # Check if pivot is within the array -> check if the end < start.
        # 2 cases
        # 1. pivot not in other array -> normal binary search
        # 2. pivot is in other partition -> check if it is larger than the first element to determine if it is pivoted i.e.
        # 5 6 7 1 2 3 4 -> target is 7. but other partion has the pivot. we check with first element 5 to determine where it is
        # 3 4 5 6 7 1 2 -> target is 1. should be on the left but the other partition has the pivot. We compare with first element 3 and realise that it is on the right.

        def modified_b_search(nums, left, right, target):
            # base case
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if (left >= right):
                return -1

            # should be on the left
            if nums[mid] > target:
                # If pivot is on the right and target should be on the right partition
                if nums[right] >= target and nums[right] < nums[mid]:
                    # 3 4 5 6 7 1 2 -> target 1
                    # right partition
                    return modified_b_search(nums, mid + 1, right, target)
                else:
                    # left partition
                    return modified_b_search(nums, left, mid - 1, target)
            # should be on the right
            else:
                if nums[left] <= target and nums[left] > nums[mid]:
                    # 5 6 7 1 2 3 4 -> target 6
                    # left partition
                    return modified_b_search(nums, left, mid - 1, target) 
                else:
                    # right partition
                    return modified_b_search(nums, mid + 1, right, target)

        return modified_b_search(nums, 0, len(nums) - 1, target)

    def searchItr(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
