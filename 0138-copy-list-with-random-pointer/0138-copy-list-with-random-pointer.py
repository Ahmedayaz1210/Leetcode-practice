"""
UNDERSTAND:
- Input; Given a singly LL
- This list has an addtional random pointer which points to any random node in the LL or None, all nodes still have their original next pointers with an addtional random one
- Have to make a deep copy of this LL which is exactly the same copy but any node from original list is not pointing to any node in new LL
- Each node has [val, random_index]
- Is this still considered a singly LL?
- Does LL still have a next pointer pointing to adjacent next or has it been replaced by random next?
- Are all node values integers
- So in a deep copy, it's exact same but no nodes from two lists point to the other list's nodes
- How big is each LL going to be? How many nodes?
- Time constraints?
- Space constraints? 
- What should the output be if the input linked list is empty (i.e., n = 0)? 
- Should it return null or an empty list?
- How should we handle the case where all random pointers are null (i.e., no random pointers exist)?
- What if the list contains only one node?
- Are random pointers allowed to point to the same node (i.e., multiple nodes pointing to a single node's random pointer)?
- Can a random pointer point back to the same node (i.e., X.random --> X)?
- Deep copy is allocating new memory
- Only difficulty comes from random pointers
- Confusing part is how can you assign a random pointer to a node if it's deep copy hasn't been created yet

MATCH: 
- Confusing part is how can you assign a random pointer to a node if it's deep copy hasn't been created yet
- We will use hashmap to store position of each node
- Map every old node to the new copy

PLAN:
- We use two passes so two loops to go through the whole LL
- First pass just creates a deep copy of all of the nodes so it's easier to navigate with random pointers
- Second pass does the pointer connecting
- Leverage hashmap to map old node to the new node

EVALUATE:
- Both time and space complexity are O(n)
- The two passes are O(n) + O(n) for TC
- I feel dumb after watching the video on this solution, it was a bit hard but I still feel like I could've solved it
- Trickiest part was of using two passes and first one just to create a deep copy of the nodes

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]