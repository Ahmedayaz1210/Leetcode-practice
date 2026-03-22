'''
Understand:
- Given head of a node and an int n
- Have to remove nth node from end of list
- The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
- Guaranteed to have at least one node and n will always be smaller than or = to num of nodes
- If we have one node, obv n will be 1, we remove than node and return none so have to remember this

Match:
- I mean Brute force way has to be reverse the LL and the remove the nth node from there by traversing n times once reversed, that would be O(n)
- The reason why this is a medium problem is to see if we can do this in one pass
- For that we can use a two pointer approach, first pointer starts as a dummy on none which points to head and second one starts n nodes away from head
- Now once second pointer reaches none at the end, we know first one is just one behind the nth node since we started it at dummy one behind head so now we can point the first's next which right now is pointing to the node we are trying to remove, and now will be pointing to it's next so the connection can be cutoff and that nth node is removed, this is the reason why we created the dummy node

Plan:
- create dummy node with val 0, point it to head and put the start pointer there
- create end pointer at head, traverse it n times
- now while end pointer does not reach none, keep moving both pointers
- now once out of while, point start to it's next's next and the connection has been cutoff
- return the dummy.next back

Evaluate:
- Pretty easy problem, got it myself, just had confusion here but figured it out myself
so first i returned head back but it didnt work for 

Example 2:

Input: head = [1], n = 1
Output: []


which made sense because head is still on node 1 and even tho its cut off its not deleted so it returned it back

but when i returned dummy.next it fixed it, how, oh wait i get it even tho start and dummy are two different vars they point to same address of dummy so if start changes the next so will dummy get affected

- TC: O(n)
- SC: O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        start = dummy

        end = head
        for i in range(n):
            end = end.next
            
        while end:
            end = end.next
            start = start.next

        start.next = start.next.next

        return dummy.next
