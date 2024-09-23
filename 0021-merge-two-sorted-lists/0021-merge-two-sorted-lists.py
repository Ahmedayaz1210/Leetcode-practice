'''
UNDERSTAND:
- Input: Two sorted LL, list1 and list2
- Both LL are sorted
- We need to merge them together and make it into one merged sorted LL
- Loop over both lists and compare their corresponding position nodes and place the smaller one before larger one in the merged list
- list1 and list2 same length? no
- If one is bigger: when the smaller LL finishes, you append the larger ones all remaining nodes as is to the merged list
- Empty lists? return empty lists
- Time constraint?
- Space constraint?
- Is node.val only going to be ints? Yes
- How big can each int be?
- How big can one LL be? 
- Both always going to be sorted
- How do we handle same node values? Doesn't matter
- Not always going to be corresponding nodes

MATCH:
- Obv LL question

PLAN:
- Create merged_list 
- Loop over the lists until one of them reaches null
- Will be a while loop because we need to handle our pointers based off of a comparison statement
- Place pointers on both lists
- Check if one is smaller than the other
- Append the smaller one to the merged_list and increment it
- In the end if either of the two lists have any nodes remaining append to the merged_list

EVALUATE:
- I was able to solve the question, the only thing I messed up was I used "or" instead of "and" in while loop because we only need to check if we have looped over one of them
- n is the length of list1 and m is the length of list2
- Time complexity: O(n+m)
- Space Complexity: O(1)
'''
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
        
        while l1 != None and l2 != None:
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

