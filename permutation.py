class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # BCR O(N*N)

        result = []

        numDict = dict.fromkeys(nums, False)

        def backtrack(numDict, selected):
            if len(selected) == len(nums):
                result.append(list(selected))

            for key, item in numDict.items():
                if item:
                    continue
                selected.append(key)
                numDict[key] = True
                backtrack(numDict, selected)
                numDict[key] = False
                selected.pop()

        backtrack(numDict, deque())
        return result
