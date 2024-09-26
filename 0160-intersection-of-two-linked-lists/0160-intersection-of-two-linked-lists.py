# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        a_pointer = headA
        b_pointer = headB
        record_a = set()
        
        # Traverse list A and record the nodes
        while a_pointer:
            record_a.add(a_pointer)
            a_pointer = a_pointer.next

        while b_pointer:
            if b_pointer in record_a:
                return b_pointer
            b_pointer = b_pointer.next
        return None