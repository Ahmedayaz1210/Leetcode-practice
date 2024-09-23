# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = ListNode(0)
        current = merged_list
        l1 = list1
        l2 = list2
        m = []
        while l1 != None and l2 != None:
            m.append(current.val)
            print(m)
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1 is not None:
            current.next = l1
        else:
            current.next = l2
        
        return merged_list.next

