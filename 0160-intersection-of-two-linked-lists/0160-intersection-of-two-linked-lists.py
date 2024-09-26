# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        if not headA or not headB:
            return None  # If either list is empty, there can't be an intersection

        # Initialize two pointers for each list
        pointerA = headA
        pointerB = headB

        # Traverse both lists
        while pointerA != pointerB:
            # Move to the next node or switch to the head of the other list
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        # If they meet, return the intersection node, otherwise return None
        return pointerA

        # a_pointer = headA
        # b_pointer = headB
        # record_a = set()
        
        # Traverse list A and record the nodes
        # while a_pointer:
        #     record_a.add(a_pointer)
        #     a_pointer = a_pointer.next

        # while b_pointer:
        #     if b_pointer in record_a:
        #         return b_pointer
        #     b_pointer = b_pointer.next
        # return None