class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Realise that if nums can be partitioned into two subsets with equal value

        # n is the index of the last element to be considered
        # we are going to find if the target can be summed from any combination of the array (at each step we consider both - include or exclude the ith element)
        @lru_cache(maxsize=None)
        def isSum(nums, n, target):
            # returns false if not sum
            if target == 0:
                return True

            if n == 0 or target < 0:
                return False

            return isSum(nums, n - 1, target - nums[n]) or isSum(nums, n - 1, target)

        totalSum = sum(nums)
        if totalSum % 2 == 1:
            return False

        target = totalSum / 2

        return isSum(tuple(nums), len(nums) - 1, target)

    def canPartitionBottomUp(self, nums: List[int]) -> bool:
        # array[n][subsetSum] is used to store the result of the calculations

        n = len(nums)

        totalSum = sum(nums)

        if totalSum % 2 == 1:
            return False

        target = totalSum // 2

        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            curr = nums[i - 1]
            for j in range(target + 1):

                if j < curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]

        return dp[n][target]
