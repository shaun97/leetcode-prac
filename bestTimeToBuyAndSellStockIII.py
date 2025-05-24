class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # We will use two arrays to represent the dP table
        # left and right where left represents the max_profit from 0 to element i 
        # right where it represents the max_profit from i to N. 
        # the right array will be calculated from the right to left -> this is so that we can keep track of the running max 
        # the left array will be calculated from the left to right -> to keep track of the running min

        left = [0] * (len(prices) + 1)
        right = [0] * (len(prices) + 1)
        left_min = prices[0]
        right_max = prices[-1]
        last_elem = len(prices) - 1
        for i in range(1, len(prices)):
            left_min = min(left_min, prices[i])
            left[i] = max(left[i - 1], prices[i] - left_min)

            right_max = max(right_max, prices[last_elem - i])
            right[last_elem - i] = max(right[last_elem - i + 1], right_max - prices[last_elem - i])

        # case where we only make one txn
        right[-1] = max(right[0], right_max - prices[0])

        max_profit = 0
        for i in range(len(right)):
            max_profit = max(max_profit, left[i] + right[i])

        return max_profit