'''
UNDERSTAND: We are given an array of integers where cost[i] is the cost for the ith step and i is the step we are on. Our goal is to get to the last index with minimum cost and at each index we can either take one step or two steps depending on whichever is the minimum and will add minimal cost to the output. What if the array if empty? 0. How many steps or how long can cost array be? >= 2, <= 1000. What can be the min to max value for each step? >= 0, <= 999

MATCH: We need to keep track of the minimum cost at each step whether we are taking one step or two steps, depends on whichever is smaller. So for that optimal approach reason we can use DP over here.

PLAN: Firstly we make a startPoint variable to see where do we need to start from whether it's the 0th index or 1th index depending on whichever is the smaller one
loop through the array from the second index to the end
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<=2:
            min(cost)

        for i in range(2, len(cost)):
            cost[i] = cost[i] + min(cost[i-1], cost[i-2])

        return (min(cost[-1],cost[-2]))