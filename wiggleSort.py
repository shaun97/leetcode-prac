class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return

        isBig = True
        for i in range(1, len(nums)):
            num = nums[i]
            if isBig:
                if num < nums[i - 1]:
                    nums[i] = nums[i - 1]
                    nums[i - 1] = num
                isBig = False
            else:
                if num > nums[i - 1]:
                    nums[i] = nums[i - 1]
                    nums[i - 1] = num
                isBig = True