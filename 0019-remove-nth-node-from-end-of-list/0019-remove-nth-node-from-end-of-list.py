# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next
        
        toRemove = len(nodes) - n
        if n <= len(nodes):
            if n == len(nodes):  
                return head.next
            nodes[toRemove - 1].next = nodes[toRemove].next
        
        return head