'''
Understand:
- Given head of a LL, we need to find if the LL has a cycle in it
- What determines a cycle is if the tail of LL (not told) points back to a node in the LL
- The var pos tells which node tail points too and pos basically stores index of it in memory to validate answer, basically this is to tell you how it works under the hood but pos is not given
- Return True if a cycle exists else False
- Check constraints
- Can we have duplicate val nodes? Yes this is not depended on node.val this is dependent in memory if tail points to that same pos node, so two nodes can have same val
- What happens if we have no nodes? Return True or False. False since points to none
- If we have one node, according to example 3 we return False so that makes sense

Match:
- Brute force way is to store all nodes, let's say in a hash set with their memory address so we are not relying on node.val and see if we encounter a node twice by going next
- But can we improve on O(n) SC? Yes we cna use the fast and slow pointer approach, one pointer loops over two nodes and other once, so if at any time both meet at same place we know that a cycle exists

Plan:
- slow = head
- fast = head
- while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
return False

Evaluate:
- Very easy problem because I know about slow and fast pointers, just needed help with if fast.next is None then when we try to access it's next we get none type error, so for that in while we check both fast and fast.next because if first fast.next == none then we know jump to false automatically
- SC: O(1)
- TC: O(n)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False