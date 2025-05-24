class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # at each step, we recurisvely call index - 1 and index - 2 to get the optimal choice for the current step (if we take index-2 + itself or index-1 without itself)
        # DP the array
        # Handle the circular loop

        def robRecurse(index, start, nums, dp):
            if dp[index] != -1:
                return dp[index]

            if index == start:
                dp[index] = nums[start]
                return dp[index]

            if index == start + 1:
                dp[index] = max(nums[start], nums[start + 1])
                return dp[index]

            dp[index] = max(robRecurse(index - 1, start, nums, dp),
                            robRecurse(index - 2, start, nums, dp) + nums[index])
            return dp[index]

        dp1 = [-1] * len(nums)
        dp2 = [-1] * len(nums)

        res1 = robRecurse(len(nums) - 1, 1, nums, dp1)
        res2 = robRecurse(len(nums) - 2, 0, nums, dp2)
        return max(res1, res2)
