'''
UNDERSTAND:
- Input: Given a singly LL
- Have to rearrange the LL
- Such that LL starts with the first node - > last node -> second node -> second to last node and so on
- L0 -> Ln -> L1 -> Ln-1 and so on
- Only move the nodes and not just values within the nodes
- Time constraints?
- Space Constraints? 
- All node values are going to be integer?
- Singly LL
- Only given the head
- How long can LL be? 1 - 5 * 10 ^ 4
- Node.val is >= 1 and <= 1000

MATCH:
- We can Use slow pointer and fast pointer approach probably
- Can also use the pattern of reversing the LL somewhere in between

PLAN:
- We can use a dequeue approach as brute force for O(n) space and time
- Dequeue helps us remove and add from both sides
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        reorder = deque()

        curr = head
        
        while curr:
            reorder.append(curr)
            curr = curr.next

        curr = reorder.popleft()
        toggle = True

        while reorder:
            if toggle:
                curr.next = reorder.pop()
            else:
                curr.next = reorder.popleft()
            curr = curr.next
            toggle = not toggle

        curr.next = None
