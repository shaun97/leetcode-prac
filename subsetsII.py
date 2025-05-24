class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        resSet = set()
        resSet.add(())
        for num in nums:
            tempSet = set()
            for item in resSet:
                itemList = list(item)
                itemList.append(num)
                itemList.sort()
                tempSet.add(tuple(itemList))
            resSet = resSet.union(tempSet)
        res = [list(item) for item in resSet]
        return res
