class Solution:
    # O(n^2)
    def twoSumN2(self, nums: List[int], target: int) -> List[int]:
        # loop through the array o(n), for each element, loop through the remaining
        # numbers and check if the sum of it equals the target
        length = len(nums)
        for x in range(0, length):
            for y in range(x + 1, length):
                if (nums[x] + nums[y]) == target:
                    return (x, y)

    # o(nlogn)
    def twoSum2Ptr(self, nums: List[int], target: int) -> List[int]:
        # sort the array -> o(nlogn)
        # two pointers referencing the start and the end of the array
        # if current sum is greater than the target, we decrease the right pointer
        # if current sum is less than the target, we increase the left pointer
        sortedVal = sorted(nums)

        lhs = 0
        rhs = len(sortedVal) - 1

        lhsVal = -1
        rhsVal = -1
        res = []

        for i in range(len(sortedVal)):
            sum = sortedVal[lhs] + sortedVal[rhs]
            if sum == target:
                lhsVal = sortedVal[lhs]
                rhsVal = sortedVal[rhs]
                continue
            elif sum < target:
                lhs = lhs + 1
            else:
                rhs = rhs - 1

        for idx, num in enumerate(nums):
            print(idx, num)
            if num == lhsVal:
                res.append(idx)
            elif num == rhsVal:
                res.append(idx)

        return res

    # O(n) time and space
    # Pass through the list and store the value as the key and index as value
    # Look through the list and find the complement and check if it exist in the hashmap
    # Make sure that it is not the same element
    def twoSum2PassHash(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hashmap and hashmap[comp] != i:
                return [i, hashmap[comp]]

    # Same as the 2 pass solution but look back at the prev hashmap as u iterate through 
    def twoSum1Pass(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hashmap:
                return [i, hashmap[comp]]
            hashmap[nums[i]] = i
