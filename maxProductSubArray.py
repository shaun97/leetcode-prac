class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        max_product = max_so_far

        for i in range(1, len(nums)):
            temp_max = max(nums[i], max_so_far * nums[i], min_so_far * nums[i])
            min_so_far = min(nums[i], min_so_far *
                             nums[i], max_so_far * nums[i])
            max_so_far = temp_max

            max_product = max(max_product, max_so_far)

        return max_product
