'''
UNDERSTAND:
- Input: We are given heads of two singly LL
- Have to find the intersection node between them
- So the node where both the singly LLs intersect
- If no intersection we return Null
- Else return intersection node
- LLs must retain their original structure after the function returns
- Value of a node is going to be an int value
- How big can headA and headB be? >= 1 and <= 3 * 10 ^ 4
- Singly LL?
- It's about finding the node not the same value because check example 1
- Time Complexity?
- Space Complexity? 

MATCH: 
- Trying to find something specifically we can use hashing for it, to distinct it out from the whole problem
- What makesit tricky is that both LL are not the same length so you can't just move pointers at the same time

PLAN:
- Run a loop over a and append every node in a hashset
- Run a loop over b and see if each node exists in the hashset or not
- if so return it
- else keep looping
- return None

EVALUATE:
- Solved it myself!
- Time Complexity: O(m+n)
- Space Complexity: O(m)
- Can I do this in O(1) Space?
	- Yes, I call this concept of inner cycle
	- Basically the way it works is, For example an intersection exists and we are moving both pointers at the same time
	- Once one reaches the end or None, it gets redirected to opposite LL header, this way the pointer which was looping over the smaller LL will move to larger and larger one which is 1 behind or how many ever behind will start the smaller LL later and by the time it gets to smaller's head, the other pointer will be at the same position on the other LL
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        if not headA or not headB:
            return None  # If either list is empty, there can't be an intersection

        # Initialize two pointers for each list
        pointerA = headA
        pointerB = headB

        # Traverse both lists
        while pointerA != pointerB:
            # Move to the next node or switch to the head of the other list
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        # If they meet, return the intersection node, otherwise return None
        return pointerA

        # a_pointer = headA
        # b_pointer = headB
        # record_a = set()
        
        # Traverse list A and record the nodes
        # while a_pointer:
        #     record_a.add(a_pointer)
        #     a_pointer = a_pointer.next

        # while b_pointer:
        #     if b_pointer in record_a:
        #         return b_pointer
        #     b_pointer = b_pointer.next
        # return None