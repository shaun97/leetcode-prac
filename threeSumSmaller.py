class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        def twoSumSmaller(nums, target) -> int:
            left, right = 0, len(nums) - 1
            res = 0
            while left < right:
                if nums[left] + nums[right] < target:
                    res += (right - left)
                    left += 1
                else:
                    right -= 1
            return res
        
        nums.sort()
        ptr = 0
        prev = -1000
        res = 0
        while ptr < len(nums) - 2:
            res += twoSumSmaller(nums[ptr + 1:], target - nums[ptr])
            ptr += 1
        return res