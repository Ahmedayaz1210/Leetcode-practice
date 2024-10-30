'''
UNDERSTAND:
- Input: Given root of a BT
- Have to return a list of the nodes level by level, so a sublist at each level has to be appended to our final list
Output: Return the final list with all sublists containing integer values
- LOT: At each level of the BT, we return left node(s) + right node(s)
- TC?
- SC?
- How many nodes can we have? [0,2000]
- Node.val? -1000 to 1000
- 1 node? return a sublist of that node
- No nodes return empty list

MATCH:
- Recursion

PLAN:
- Base case: if not root return []
- Initialize Result list
- Helper function to loop over left and right side 
- We want to go to next level when we have recursed over both sides
- One side can't leave the other behind, we can't have a mismatch
- Helper function(left, right):
- if not root: return

MISTAKE:
- Up until now I was using recursion but if you technically look, we should use recursion in DFS problems when we are looking to go into the depths of the question but here we want all the nodes at each level so it would be BFS
- I have never implemented BFS so using neetcode video

PLAN: 
- Use a deque for FIFO structure so root gets appended first in the result list
- Before moving to the next level we have to empty out the queue
- When you pop the node from queue, add it's children to the queue
- TC and SC: O(n)
- One question I was confused was with when we append the descendants of a node before removing it from the queue wouldn't they get appended in the loop as well? No because before appending we only loop over amount of times from the current level's number of nodes

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res