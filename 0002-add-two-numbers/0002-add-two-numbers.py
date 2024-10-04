'''
UNDERSTAND:
- Input: Given two singly LL
- Each node has a single digit integer value
- Throughout the LL, if you append all nodes values together as a string it makes up one number
- You do the same for the other LL and you have two numbers
- Now you take these two numbers and sum them
- Then their sum is broken down into number by number and you make a LL from it, so each character or integer inside the number is put inside a node and those nodes form a LL, all in sequences
- Now the two input LL we are given are in reverse order, when we convert LL to a number, we have to reverse that number
- when we do the sum, we reverse it back and then make a result LL out of it since original LL were reversed
- All the numbers are going to be non negative integers
- I am assuming we won't be given 0's at the start or end so we don't have any leading 0s
- How many nodes will each LL have? [1,100]
- How big is each int val going to be? 0 - 9
- Are both LL going to be of the same length? No
- If we have 0 do we return back 0? Yes

MATCH:
- Don't think need any DS or Algo here

PLAN:
- Loop through both of the lists
- Take each value and append it to a string
- Reverse the string and convert it to a number
- Add the two numbers
- Take the number, convert it to a string, reverse it, convert back to an int
- Run a loop, make new nodes for each value, append the value and create our LL

EVALUATE:
- Got the question within 27 minutes
- Feel like I could have done this in 10 minutes
- Pretty strightforward
- Time Complexity: O(n + m)
- Space Complexity: O(1)
- My solution is pretty ok, there is a better way to do this which neetcode showed where we only use one loop
- My code:
        cur1 = l1
        num1 = ''
        while cur1:
            num1 += str(cur1.val)
            cur1 = cur1.next
        num1 = int(num1[::-1])
        
        cur2 = l2
        num2 = ''
        while cur2:
            num2 += str(cur2.val)
            cur2 = cur2.next
        num2 = int(num2[::-1])
        
        sumOfLL = str(num1 + num2)
        sumOfLL = sumOfLL[::-1]

        dummy = ListNode(0)
        cur = dummy
        for i in range(len(sumOfLL)):
            strToint = int(sumOfLL[i])
            cur.next = ListNode(strToint)
            cur = cur.next

        return dummy.next
        
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0

            val = d1 + d2 + carry
            carry = val // 10
            cur.next = ListNode(val % 10)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
