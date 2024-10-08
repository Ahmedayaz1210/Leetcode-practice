'''
UNDERSTAND:
- Input: nums array which contains n + 1 integers
- n is the biggest integer value in our array, all the integers (elements) in our array are between range [1,n] 
- All exist once besides one integer which repeats twice
- Length of our array is always n+1, so even if all integers exist between [1,n] that n + 1 integer will be our duplicate
- Have to find that duplicate
- Hard part is we can't alter the array like sort it
- Only have to use Constant space
- How big can n be? 1 - 10^5 inclusive
- How big can nums be? n+1
- Each integer is between 1 and n inclusive
- Time Constraints? O(n)
- Space Constraints? O(1)
- What if n = 1, then we would just have 1?
- Always have one eaxct duplicate? Yes
- All numbers are same could be edge case
- Repeated one exists twice or more time

MATCH:
- This is a LL cycle
- Use floyd's algorithm
- Maybe use slow pointer, fast pointer here because at some point since there is only one number which is being duplicated exists, both pointers will point to same number

BF:
- Take each number and check if it exists later in array

PLAN: 
- The trick is since all the values are between [1,n] they all point to a position inside the array so two numbers are going to point at the duplicate value, which means there will be a cycle if you visualize it as a cycled LL
- Example 1 in LL: 0 -> 3 -> 2 -> <- 4
- For a better understanding, watch the video I recorded, it's lengthy to write her

The trick how second loop works, used claude:

1. Structure of the array:

There's a "non-cyclic" part (if any) leading to the cycle
The duplicate number is always at the entrance of the cycle


2. After the first loop:

The fast pointer has gone around the cycle at least once
Both pointers meet at some point in the cycle (not necessarily the duplicate)


3. Key insight:

The distance from the start of the array to the cycle entrance
is equal to
The distance from the meeting point to the cycle entrance (going around the cycle)


4. Second loop mechanism:

We move the slow pointer to the start of the array
We keep the fast pointer at the meeting point
We move both one step at a time


5. Why it works:

Slow pointer travels: Start -> Cycle Entrance
Fast pointer travels: Meeting Point -> Cycle Entrance
These distances are equal (from our key insight)
So they meet exactly at the cycle entrance (our duplicate)
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return fast