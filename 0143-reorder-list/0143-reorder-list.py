'''
Understand:
- Given head of a LL
- Have to rearrange the LL in a way such that we put first node then we point it to last node, then we point it to 2nd node and that points to n-1 node, n being last
- We cannot change it by values, we have to point by node addresses
- From examples seem like node.val goes in increasing order but since vals are irrelevant, I can ignore that
- The number of nodes in the list is in the range [1, 5 * 104].
- 1 <= Node.val <= 1000

Match:
- I mean brufte force way i can think of it is looping the whole LL, storing all nodes and rearranging so thats O(n) sc and O(n) tc 
-maybe we can use two pointers here too? so kind of one starts at head and for tail we first loop all the way till end of LL, oh wait maybe we have to use the logic of reversing a LL here? so could it be reverse + merge two LLs logic?
- How about taking the LL in half, keep the first half and reverse the second half
- Then from there we can merge both using merging logic from previous question 
- One thing to keep track of is, we need to split them in half so when we find the middle, we have to identify it's previous and make it point to none, this way it's O(n) two separate for loops not nested and O(1) sc
- also this merging is strictly alternating not based of node.val

Plan:
let's have a split and reverse function
- headTwo = head
- endTwo = head
- prev = head
- while endTwo and endTwo.next:
    - prev = headTwo
    - headTwo = headTwo.next
    - endTwo = endTwo.next.next
- prev.next = None
curr = headTwo
prev = None
- while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt

merge function takes headtwo and head
headone = head
- while headone and headtwo:
    nxt1 = headone.next
    headone.next = headtwo
    headone = nxt1
    nxt2 = headtwo.next
    headtwo.next = headone
    headtwo = nxt2

Evaluate:
- So I couldn't get the logic, it was hard to find out that we need to split in half, reverse second half and merge alternatively
- I tried the code, got 90% of it, but for some reason it wasn't working on example 2, it kept missing the 3 in the end so it wasn't working on odd nodes
- I looked up the solution and this solution was much simpler but i got the code most of it on my solution but it was just too messy
- TC: O(n)
- SC: O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Second half of the list
        second = slow.next
        # Splitting so first half's last node needs to point to None
        slow.next = None

        # Reversing
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Merging both halves
        # first is head of the first half and since second was reversed, it's head is the last node which is on prev
        first, second = head, prev
        while second: #according to our code second will always be smaller in odd nodes
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        
        
        