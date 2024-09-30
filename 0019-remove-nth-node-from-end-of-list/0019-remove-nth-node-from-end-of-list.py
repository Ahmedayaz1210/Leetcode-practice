# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        behind, forward = head, head

        for i in range(n):
            forward = forward.next

        if not forward:
            return head.next

        while forward.next != None:
            behind = behind.next
            forward = forward.next


        behind.next = behind.next.next
        return head
        
