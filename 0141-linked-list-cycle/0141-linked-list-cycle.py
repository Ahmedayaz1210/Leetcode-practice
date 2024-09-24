'''
UNDERSTAND:
- Input: Given head of a singly LL
- Have to find cycle in that LL
- If any node is being pointed at twice, position variable (have to check ourselves)
- Cylced Node is being pointed at from the tail node
- Output: Return True if cycle found, else False
- How long can the LL be? 
- Only one node is going to be pointed at twice? 
- So only one cycle?
- All the values are going to be integers?
- How big can an integer be?
- Time Constraints?
- Space Constraints?
- What if no node or only one? Return false for no node, maybe check if the only one node's next is itself
- Can any value repeat or is every node going to have a distinct value?

MATCH:
- Keep track with help of position, so we need to remember the positions
- We can probably use a list for it
- NO UPPER SOLUTION IS WRONG
- how about using a fast and slow pointer
- Slow moves one at a time and Fast moves twice, at one point they are going to meet, so we know it is a cycle
- Because both will continuously be looping

PLAN:
- If LL length is 0 return False
- Run a while loop until it's true
- Create a checked boolean list which checks if we have already went over a certain position
- Create a current counter and the current counter position in boolean list changes to True
- Increment the current counter
- NEW APPROACH:
- Create a slow and fast pointer
- create a while loop to check if fast and it's next is not None
- slow jumps by one node and fat jumps by two nodes
- Check if they ever == each other

EVALUATE:
- My hash set approach was valid as well of storing nodes
- I just made a mistake in while loop else code was correct, I was checking if both slow and fast are none or not, when it should be fast and fast.next, check comment in code for explanation
- Time: O(n)
- Space: O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head.next is None:
            return False

        slow, fast = head, head

        while fast is not None and fast.next is not None:  # Ensure both fast and fast.next are valid, the reason why we check fast.next is because even if fast.next.next is None, after this loop where fast will move twice, it will always land on None and in next loop check it will be terminated
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
