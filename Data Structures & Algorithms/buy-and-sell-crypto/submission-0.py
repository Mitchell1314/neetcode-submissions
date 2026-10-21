class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for i in range(0, len(prices)):
            min_price = min(min_price, prices[i])
            profit = prices[i] - min_price
            max_profit = max(profit, max_profit)
        return max_profit
              


        