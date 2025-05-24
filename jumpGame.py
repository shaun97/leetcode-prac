class Solution:
    def canJumpDPMAYTLE(self, nums: List[int]) -> bool:
        # Bottom up dp -> array of length nums where the ith element is whther we can reach the end from that position. As long as the
        # curr position can reach that position and beyond, it will be g
        if len(nums) == 1:
            return True

        lastIndex = len(nums) - 1
        dp = [0] * (lastIndex + 1)
        dp[lastIndex] = 1  # 1 means yes, 0 means uncalculated, -1 means no

        # we build it from the back
        for i in range(lastIndex - 1, -1, -1):
            steps = nums[i]
            if steps + i >= lastIndex:
                dp[i] = 1
                continue

            for step in range(1, steps + 1):
                if dp[step + i] == 1:
                    dp[i] = 1
                    break
        return dp[0] == 1

    def canJumpGreedy(self, nums: List[int]) -> bool:
        # We dont need to store all the good indexes, we just need to know the left most good index, if our current 
        # position can reach there, we are guaranteed to reach the end! Very clean
        if len(nums) == 1:
            return True

        leftMostGood = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            steps = nums[i]
            if steps + i >= leftMostGood:
                leftMostGood = i
        return leftMostGood == 0