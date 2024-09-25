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
