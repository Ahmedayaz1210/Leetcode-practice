'''
UNDERSTAND:
- Input: Two inputs: head of LL and an integer value "n" 
- Have to remove the nth node from the end of the list
- Go to the end of LL and from there count back n times and remove that n'th node
- Remove nth node from "None"
- Singly LL
- n always < len(LL)? Yes, 1 - len (inclusive)
- How long can the LL be? 1 to 30 inclusive
- How big can each node.val be? 0 to 100 inclusive
- All values of nodes are going to be ints ? Yes
- n is int? Yes
- Empty list? will have at least 1 node
- if one node n has to be 1, then we retun empty list
- Time Complexity?
- Space Complexity?

MATCH:
- Brute force approach: store everything in a list and remove nth from the last or len(list) - n, we will have original position of it
- But that is big O(n) memory
- Can be done using slow and fast pointer

PLAN:
- BF: Append eveyrthing to a list and then do len(list) - n, remove that node and make its previous point point to the node we want to remove's next
```
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
```
- Use Two pointer approach
- One pointer is behind which remain n steps behind forward pointer
- forward is initialized to head and moved n times from the start
- if forward is None after moving n steps, this means we need to remove the first node (EDGE CASE)
- we just return head.next
- else we move both pointers until forward goes to last node
- after this loop we take the behind pointer which is one previous to the node we want to remove and we make it skip that node and point to .next.next

EVALUATE:
- I was able to solve BF approach 
- For optimal, I messed up algorithm slightly by creating a prev pointer but all we needed to do was loop forward till last node not till None
- Also I didn't realize about the edge case, which was if we have to remove the head node, then we check if forward is None after n steps, if so we return head.next
- Time Complexity: O(n)
- Space Complexity: O(1)
'''
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
        
