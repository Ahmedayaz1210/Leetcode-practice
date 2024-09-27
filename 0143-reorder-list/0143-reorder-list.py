'''
UNDERSTAND:
- Input: Given a singly LL
- Have to rearrange the LL
- Such that LL starts with the first node - > last node -> second node -> second to last node and so on
- L0 -> Ln -> L1 -> Ln-1 and so on
- Only move the nodes and not just values within the nodes
- Time constraints?
- Space Constraints? 
- All node values are going to be integer?
- Singly LL
- Only given the head
- How long can LL be? 1 - 5 * 10 ^ 4
- Node.val is >= 1 and <= 1000

MATCH:
- We can Use slow pointer and fast pointer approach probably
- Can also use the pattern of reversing the LL somewhere in between
- For Brute force we can use deque so we can remove from left and right at a time

PLAN:
- We can use a dequeue approach as brute force for O(n) space and time
- Dequeue helps us remove and add from both sides
- reorder = deque()

        curr = head
        
        while curr:
            reorder.append(curr)
            curr = curr.next

        curr = reorder.popleft()
        toggle = True

        while reorder:
            if toggle:
                curr.next = reorder.pop()
            else:
                curr.next = reorder.popleft()
            curr = curr.next
            toggle = not toggle

        curr.next = None
- Optimal Approach:
- Have to somehow:
    - Split the LL into half: 

        -The way you do that is using fast and slow pointer so by the time fast pointer is on the last node or None, slow will be at the half way point where can find out that slow pointer is the middle barrier since fast moves "Twice". 
        -So slow.next will be beginning of the second half, works for both even and odd lists

    - Second half gets reversed:
        - Use the same approach as Reverse Linked List

    - Both halves get merged:
        - Remember to save the next of each pointer from both halves before breaking them off because we will need them to merge back together

    - Last node should point to None

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

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
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2





