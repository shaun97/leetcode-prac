class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort array

        # iterate through the sorted array with one pointer
        # make sure to account for duplicates

        # apply two sum to the remaining portion of the array after the ith element
        nums.sort()
        res = []
        prevElem = nums[0] - 1
        for i in range(len(nums) - 2):
            if prevElem == nums[i]:
                continue
            prevElem = nums[i]
            complement = self.twoSum(nums, i + 1, -nums[i])
            if len(complement) is not 0:
                for pair in complement:
                    res.append([nums[i]] + pair)
        return res

    def twoSum(self, nums, start, target):
        end = len(nums) - 1
        res = []
        # placeholder
        prevElem = nums[start] - 1

        while end > start:
            if prevElem == nums[start]:
                start += 1
                continue

            currSum = nums[start] + nums[end]
            if currSum == target:
                prevElem = nums[start]
                res.append([nums[start], nums[end]])
            elif currSum > target:
                end -= 1
            else:
                start += 1
        return res
