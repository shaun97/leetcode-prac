class Solution:
    def rob(self, nums: List[int]) -> int:
        # At the nth step, we have two choices, to rob or not rob this house. Due to the constraint, if we rob the house
        # we must not rob the n-1 (we need to choose the optimal decision of n-2 + the current house). If we do not
        # rob the house, we just take the optimal decision for n - 1 house.

        # dp table, index 1 refers to house 1
        dp = (len(nums) + 1) * [-1]
        dp[0] = 0
        dp[1] = nums[0]

        # we build from bottom up

        for houseIndex in range(1, len(nums)):
            dp[houseIndex + 1] = max(dp[houseIndex - 1] +
                                     nums[houseIndex], dp[houseIndex])

        return dp[len(nums)]
