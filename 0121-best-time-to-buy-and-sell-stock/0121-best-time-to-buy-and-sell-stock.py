'''
Understand:
- Given an int array called prices where prices[i] is price of a stock on a given day
- We have to return the maximum profit as an int we can make if we buy at a certain day and sell at another in future, key thing to note is you can't buy in future and sell in past, so once u buy you can only move forward over the array
- if profit is less than 0 then return 0
- How big will prices be? 1 to 10^5
- How big prices[i] will be? 0 to 10^4
- are we only dealing with ints? yes

Match:
- So basically the straight forward approach to this is taking each element and calculating it's profit with all future elements in array but this will take a lot of time it would be O(n^2)
- so l pointer on 7 and r on 1, ok so val at l is bigger than val at r which means this can't be max profit for now, so we move r pointer one over because this one keeps moving for comparison and we move l to this element or next element since it's smaller and we know this is smallest so far so now l is on 1 value i mean it has idx 1 too so whatever, then r moves to 5 value, now we compare and get a profit of 4 ok so this is max profit so far but since 5 is > 1 we don't need to move l and we just move r to calculcate next and eventually we exhaust all list and never switch l pointer since nothing was smaller than 1
- this way we can achieve O(n)

Plan:
- Check if we have at least two elements else return 0
- Have max profit = 0 variable
- Have left = 0 and r = l+1 pointers
- Run a loop with r  over the prices list:
    - compare prices[r] - prices[l], if bigger than max so far then     update max profit
    - if prices[l] > prices[r] move over l to r
- return max profit

Evaluate:
- Solved it all by myself! Even though I understood that this is not exactly a sliding window question because we don't care about elements in the window
- SC: O(1)
- TC: O(n) because we loop once and only move l under a certain condition
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        max_profit = 0
        l = 0
        for r in range(1,len(prices)):
            max_profit = max(max_profit, prices[r]-prices[l])
            if prices[l] > prices[r]:
                l = r
        return max_profit