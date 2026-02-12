'''
Understand:
- Given a list piles where i is a single pile and piles[i] is num of bananas in that pile.
- We need to find minimum number that could be used by koko to eat all bananas in h hours. 
- we return the minimum int k
- the catch is koko can eat min or less than min bananas in that pile, if a pile has less than min (k) bananas and koko manages to finish the pile before the hour koko won't move to next pile. but if a pile has more than k bananas then that pile can take multiple hours to be eaten. 
- Example 1 breakdown:
        Hour 1: Pile 1 (3 bananas) → eats all 3, done with this pile
        Hour 2: Pile 2 (6 bananas) → eats 4, leaves 2
        Hour 3: Pile 2 (2 left) → eats remaining 2
        Hour 4: Pile 3 (7 bananas) → eats 4, leaves 3
        Hour 5: Pile 3 (3 left) → eats remaining 3
        Hour 6: Pile 4 (11 bananas) → eats 4, leaves 7
        Hour 7: Pile 4 (7 left) → eats 4, leaves 3
        Hour 8: Pile 4 (3 left) → eats remaining 3
- How big can piles be?
- How big can piles[i] be?
- How big can h be? check constraints for all

Match:
- Basically we need to find MINIMUM number to exhaust the whole list within h hours.
- i notice that when piles len is 5 and h is 5 too that means each hour u need to find the biggest element which there is 30 else no way u can finish in those hours

similarly in 6 hours one, we used kind the second smallest number but at the same time yes the number doesn't have to be present in piles since 4 in first example is not

- so min could be 1 and max could be max(piles) which would take O(n) at the start but it's still best option here since piles isn't sorted so we can't make it any faster

- But this helps us because now our range is 1 - max in piles and we can run basic binary search on this number to see which number suits in h hours

Plan:
- left pointer = 1
- right = max(piles)
- now what's the main logic? what is mid value satisfying here? - so we would need a var to keep track of hours and see it doesn't cross h. then we loop over each piles element and see is mid >= piles[i] if so we add 1 to our curr hours, if its not and is bigger than we do piles[i] - mid and store it in a var let's say remaining then if we have any remaining we check mid over that and do that until it's exhausted, then we repeat the process but if at any point, curr hours goes over hours, we break out and move back to binary search to find next bigger number or if it's less than hours then we have capactiy to go down and find next smallest
- can actually use (p[i/k)ceil method this is actually faster than subtraction

Evaluate:
- I would say solved 80% of it by myself, there were some issues in code but got the logic pretty much
- TC: O(n + log(max of the pile)) because n is for looping piles and we log from 1 to max of pile because thats how big we can go
- SC: O(1)
'''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            validation = self.checkHours(mid, h, piles)
            if validation:
                right = mid - 1
            else:
                left = mid + 1
        return left
            


    def checkHours(self, mid: int, h: int, piles: List[int]) -> bool:
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile/mid)
        return total_hours <= h

