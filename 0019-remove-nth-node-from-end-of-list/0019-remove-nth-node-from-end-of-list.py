# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            # Store nodes in a list
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next
        
        # Remove nth node from end
        if n <= len(nodes):
            if n == len(nodes):  # Removing first node
                return head.next
            nodes[-n-1].next = nodes[-n].next
        
        return head