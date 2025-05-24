class Solution:
    # Brute force solution, iterate through everyday and find the maximum profit to sell for the
    # following days
    # O(n2)
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit

        return max_profit

    # Search for the lowest peak, if something is lower then replace it as the lowest
    # For any value higher than the lowest, check if max_profit is larger
    # O(n)
    def maxProfitOnePass(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit
