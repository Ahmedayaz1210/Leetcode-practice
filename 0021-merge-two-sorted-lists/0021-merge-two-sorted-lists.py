'''
Understand:
- Given head of two sorted LLs
- Have to merge them into one sorted, so curr node.val > prev node.val
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.
- We can have two nodes with same val so doesn't really matter which goes before which as long as LL follows rest of order, we might have to just check >= in the code or <= depending on which way we go

Match:
- From example 2 we can see if both LLs are empty return None I guess?
- Since we know both are sorted we don't really need to worry much about connection cutting since we know next one will always be greater 
- What we can do is taken the longer of the two and loop over it because we know longer one will just append left over nodes at the end as is or maybe we loop over shorter one, wait how do we know size of them since we are just given head nodes
- So I guess we do like while either of the heads or curr doesn't reach none, we compare the curr nodes values, now if we need to make a connection, we move curr on one LL to its next to not lose track of it and point the curr's next to other LL's curr

Evaluate:
- I overcomplicated my code, I got the logic correct, my code was good enough to only pass on screen tests but it was a bit messy when returning the head it wasn't properly checking which one to return, which is why we needed a dummy node here and this is a concept I had forgotten so it's ok I will still count as question solved
- TC: O(m + n) we loop both in worse case if they are same len
- SC: O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        curr = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        curr.next = list1 if list1 else list2
        return dummy.next
        