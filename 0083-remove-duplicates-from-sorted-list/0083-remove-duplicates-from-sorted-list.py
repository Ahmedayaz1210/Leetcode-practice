'''
UNDERSTAND:
- Input: Given a sorted LL
- Guaranteed the list we get is sorted
- Have to remove all duplicates from the LL
- Any nodes with repeated values get taken out and only one of their kind remains
- Return back the sorted list with duplicates removed
- Empty LL? Return back nothing? None?
- If no dups exist, return as is
- How long can out LL be? 0 - 300
- Our all nodes just going to have int values? Yes
- How big can each integer be inside a node? -100 to 100
- Time Constraint?
- Space Constraint?
- Do I return back head of the new LL?
- LL is only going to be singly?

MATCH:
- Hashing in this problem
- Helps us find duplicate items
- It's about finding duplicate values rather than nodes
- Hash set will be handy

PLAN:
- Start our curr pointer at head
- Check if it's already in the hashset, if so we skip over it
- Else we append it to hash set and keep track of it's previous one and make it point to current's next

EVALUATE:
- Was able to solve it in 20 minutes!
- Time Complexity: O(n)
- Space Complexity: O(n)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        check_dup = set()

        prev, curr = None, head

        while curr:
            if curr.val not in check_dup:
                check_dup.add(curr.val)
                prev = curr
            else:
                prev.next = curr.next
            curr = curr.next

        return head
