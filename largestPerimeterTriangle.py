class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()
        a = 0
        b = 1
        c = 2

        while c < len(nums):
            if nums[a] < nums[b] + nums[c]:
                break
            else:
                a += 1
                b += 1
                c += 1

        return nums[b] + nums[c] + nums[a] if c != len(nums) and (nums[b] + nums[c] > nums[a]) else 0
