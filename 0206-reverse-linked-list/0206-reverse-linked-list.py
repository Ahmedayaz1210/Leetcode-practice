'''
Understand:
- Given head of linked list we just have to reverse it
- We are only given the head
- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000

Match:
- So what we can do is loop over the LL, starting with the head, we create a var called prev to point the curr node to maintain the reverse order, we will ini it with None so head can point to none when reversing, then curr pointer becomes new prev and we can also have a next var to store curr's next before breaking the chain and move to that next node and we keep doing this until next doesn't hit None
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev