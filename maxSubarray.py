class Solution:
    def maxSubArrayBruteForve(self, nums: List[int]) -> int:
        # brute force solution O(n2)
        # loop through the array twice. one for the start index, second for the end index
        # for each start index
        # res to store the max sum
        max_val = -math.inf
        for i in range(len(nums)):
            current_val = 0
            for j in range(i, len(nums)):
                current_val += nums[j]
                max_val = max(max_val, current_val)
        return max_val

    def maxSubArrayKadane(self, nums: List[int]) -> int:
        # o(n)
        # loop through the array
        # store the current max val
        # store the total max val
        # everytime the current val goes negative, reset it back to to the next value
        curr_subarray = 0
        max_subarray = -math.inf
        for i in range(len(nums)):
            if curr_subarray < 0:
                curr_subarray = nums[i]
            else:
                curr_subarray += nums[i]
            max_subarray = max(curr_subarray, max_subarray)
        return max_subarray

    def maxSubArrayRecursion(self, nums: List[int]) -> int:
        # o(nlogn)
        def findBestSubArray(nums, left, right) -> int:
            # split the array into half, sum the lhs, rhs.
            # check which subarray lhs + rhs + mid give the largest value
            # check if there are larger subarrays within the left and right using recursion
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr = 0
            best_left = 0
            best_right = 0

            # sum lhs from the middle, we want to check what is the largest subarray we can form starting from the middle
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left = max(best_left, curr)

            curr = 0
            # sum rhs from middle to end
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right = max(best_right, curr)

            # best lhs and rhs without middle will be settled using recursion
            best_combined = nums[mid] + best_right + best_left

            left_half = findBestSubArray(nums, left, mid - 1)
            right_half = findBestSubArray(nums, mid + 1, right)

            return max(left_half, right_half, best_combined)

        return findBestSubArray(nums, 0, len(nums)-1)
