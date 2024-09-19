'''
UNDERSTAND:
- Input: Given a singly linked list
- Output: return the reverse of the singly linked list
- Basically we have to reverse or flip all elements in an array or linked list
- For example element at 0 goes to last place, element at position 1 goes to second last, so on and so forth
- Time constraints?
- Space constraint?
- How long can the linked list be? Can have 0 - 5000 nodes
- Is the LL only going to have integers? Yes
- How big can each int or element be? -5000 to 5000 inclusive
- What if given empty LL? return []
- Do I need to reverse the list in-place, or can I create a new list with reversed elements?
- What should happen to the original list after the reversal? Should it remain unchanged or modified?

MATCH:
- Since it's LLs we can use LLs to solve this

PLAN:
- Create a second LL or array
- Create a dummy head on result LL to help us return it and reference the first node
- Loop over our input LL 
- Append our current node to our result LL and each time we append at the start so it creates a reversed version
- Append it after dummy head
- In the end return the node next to dummy head

EVALUATE:
- **Iterative approach**
- First Question on Linked List topic so a lot of mistakes and incorrect logic for the question
- Firstly we don't both a result array and a dummy head, the dummy head alone can help us
- Secondly we kind of use a two pointer approach of a previous and current counter
- The previous counter stores the node which we want our current node to point, because when the current node points to previous which in other words is when current node points backwards or goes in "reverse" and that's what we want, have all nodes point backward
- Also we need to store our current nodes next node because once current node points backward, it's connection with it's next node will break so if we store next one before breaking the connection or the chain, later when moving the current to next node we can use our next variable
- Time Complexity: O(n) since looping through the whole Linked List
- Space Complexity: O(1) since all we use are pointers to do this
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


