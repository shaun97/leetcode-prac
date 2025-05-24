class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(comb, start, target):
            if sum(comb) == target:
                res.append(list(comb))
                return
            if sum(comb) > target:
                return

            for i in range(start, len(candidates)):
                if candidates[i] + sum(comb) > target:
                    return
                comb.append(candidates[i])
                backtrack(comb, i, target)
                comb.pop()

        backtrack([], 0, target)
        return res
