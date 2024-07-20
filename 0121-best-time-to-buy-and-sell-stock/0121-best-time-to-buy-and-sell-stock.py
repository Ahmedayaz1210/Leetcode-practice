class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            current_profit = price - min_price
            if current_profit > max_profit:
                max_profit = current_profit

        return max_profit
