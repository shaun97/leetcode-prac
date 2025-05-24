class Solution:
    # Recursive Optimized Memoizded solution
    def superEggDrop(self, k: int, n: int) -> int:
        # At each step we have two options from 0 - n
        # The egg breaks and we need to search from 0 - i using k - 1 eggs
        # The egg doesnt break and we go to the next step to drop an egg with k eggs
        dp = [[-1] * (n + 1) for _ in range(k + 1)]

        # takes in noOfEggs and rangeOfNums
        # returns the min number of moves needed for that number of eggs and rangeOfNums
        def superEggDropR(noOfEggs, rangeOfNums) -> int:
            if rangeOfNums == 1 or rangeOfNums == 0:
                return rangeOfNums
            if noOfEggs == 1:
                return rangeOfNums

            if dp[noOfEggs][rangeOfNums] != -1:
                return dp[noOfEggs][rangeOfNums]

            minMoves = 10**10

            # We need to optimise this part -> not binary search but another dp
            left, right = 1, rangeOfNums - 1
            while left <= right:
                mid = left + (right - left) // 2
                eggBreak = superEggDropR(noOfEggs - 1, mid - 1)
                eggNoBreak = superEggDropR(noOfEggs, rangeOfNums - mid)
                if eggBreak == eggNoBreak:
                    minMoves = min(minMoves, 1 + max(eggBreak, eggNoBreak))
                    break
                elif eggBreak > eggNoBreak:
                    right = mid - 1
                else:
                    left = mid + 1
                minMoves = min(minMoves, 1 + max(eggBreak, eggNoBreak))

            dp[noOfEggs][rangeOfNums] = minMoves
            return dp[noOfEggs][rangeOfNums]

        res = superEggDropR(k, n)
        return res


