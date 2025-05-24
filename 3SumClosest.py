class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # we sort the array and use 2 sum
        # we use 1 pointer and run 2sum on the rest of the array
        first = 0
        best = 10 ** 5
        nums.sort()

        while first < len(nums) - 2:
            second = first + 1
            third = len(nums) - 1
            while second < third:
                currSum = nums[first] + nums[second] + nums[third]
                if abs(currSum - target) < abs(best - target):
                    best = currSum
                if currSum > target:
                    third -= 1
                elif currSum < target:
                    second += 1
                else:
                    return currSum
                
            first += 1
        return best