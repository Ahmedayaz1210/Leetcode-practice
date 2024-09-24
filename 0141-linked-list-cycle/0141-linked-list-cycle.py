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
        
        while fast is not None and fast.next is not None:  # Ensure both fast and fast.next are valid
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
