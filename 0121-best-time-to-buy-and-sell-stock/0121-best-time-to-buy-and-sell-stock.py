'''
UNDERSTAND:
- Given an array of integers "prices"
- Where prices[i] is price of a stock on the ith day
- Have to find the maximum profit of buying a stock one day and selling it in future (has to be future, can't track back once bought)
- Buy at the minimum price and sell at the maximum future price
- Buying and selling has to be DIFFERENT days
- output: max profit
- Clarifying questions: min and max length of the array? 1 - 10^5
- Can we have an empty array?
- With the one element in the array how can we buy and sell on different days?
- Each integer can be between 0 and 10^4
- Lowest a max profit can be is 0

MATCH: 
- For max and min problems we can use, DP, Greedy or sliding window
- Sliding window works best because we have to keep track of both the min price and maxprofit so we can create a window of it


PLAN: 
- Left pointer at 0 index, right at 1 index 
- if current index is smaller than min variable, that's our new min
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minNum = prices[0]
        maxProfit = 0
        for p in prices:
            if minNum > p:
                minNum = p 
            maxProfit = max(maxProfit, (p - minNum))

        if maxProfit < 0:
            maxProfit = 0
        return maxProfit
            