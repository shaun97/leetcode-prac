class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # lhs array will contain the product of all the elements of either the left of the current index i
        # Loop through all the numbers from left to right, form the lhs array
        # r will contain ongoing product of values as we traverse right to left
        # Combine all the values
        length = len(nums)

        lhs = [1] * length
        result = [1] * length
        r = 1

        for i in range(1, length):
            lhs[i] = lhs[i - 1] * nums[i - 1]

        for i in range(length - 1, -1, -1):
            result[i] = lhs[i] * r
            r = r * nums[i]

        return result
