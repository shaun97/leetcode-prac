class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictCheck = {""}
        for num in nums:
            if num in dictCheck:
                return True
            else:
                dictCheck.add(num)
        return False
