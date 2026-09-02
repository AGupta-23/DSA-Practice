class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        max_profit = 0
        min_price = float("inf")

        for i in range(0,n):
            if prices[i] < min_price:
                min_price = prices[i]
            profit = prices[i]-min_price
            max_profit = max(max_profit, profit)
        return max_profit