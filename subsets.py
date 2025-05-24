class Solution:
    def subsetsC(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = [[]]
        # []
        # Consider 1
        # [] + [1]
        # Consider 2
        # [] + [1] + [2] + [1, 2]
        # Consider 3
        # [] + [1] + [2] + [1, 2] + [3] + [1, 3] + [2, 3] + [1, 2, 3]
        for num in nums:
            res += [curr + [num] for curr in res]
        return res

    def subsetsB(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output
