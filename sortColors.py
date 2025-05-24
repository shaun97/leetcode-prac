class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(first, second, array):
            temp = array[first]
            array[first] = array[second]
            array[second] = temp

        p0 = 0
        curr = 0
        p2 = len(nums) - 1
        while p2 >= curr:
            if nums[curr] == 0:
                swap(curr, p0, nums)
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                swap(curr, p2, nums)
                p2 -= 1
            else:
                curr += 1

    def sortColorsCountingSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = {0: 0, 1: 0, 2: 0}  # we do counting sort

        for num in nums:
            counter[num] += 1

        index = 0
        for key, items in counter.items():
            for i in range(items):
                nums[index] = key
                index += 1
