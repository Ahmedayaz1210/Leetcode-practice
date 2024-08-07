'''
UNDERSTAND: We are given an array of prices for a stock for certain amount of days and we have to find what is the best time to buy a stock and then LATER after buying when is the best time to sell it. i represents day(s) and prices[i] represents the price of the stock for ith day. Also if there is no profit we can just return 0. what if we are just given an empty arrya? Still 0? how many days can we have in total or length of prices? What is the range of prices? >= 0, <= 10^4.

MATCH: We can use Two pointer approach but wouldn't be the best since it can take a lot of time complexity. So in order to save time we can tradeoff space complexity and use Dynamic Programming so we can save all the previous answers and in the end choose the one highest profit

PLAN: We can keep track of the minimum profit we have as well as the maximum profit we have. As we loop through the array we can keep track of minimum and maximum profit. We can update our maximum profit. return max profit
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for p in prices:
            minPrice = min(minPrice, p)
            maxProfit = max(maxProfit, p - minPrice)

        return maxProfit
