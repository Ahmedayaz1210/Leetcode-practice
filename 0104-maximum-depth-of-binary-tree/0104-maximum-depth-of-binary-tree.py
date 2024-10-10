'''
UNDERSTAND: 
- Input: Given root of a binary tree
- root? the top node or parent node of all the nodes
- BT: A tree which has at max two descendants one left and one right, can be anything from no descendants to 2 descendants
- Output: Return max depth of the BT given
- Max depth: Find height of the tree or how deep does the tree goes
- Tree is represented as a sequence of nodes? Yes
- What does a node has for parameter(s)? Left, right pointers and a node.value
- Can a node value repeat? Yes
- Is a node value integer? Yes
- How big? -100 to 100 inclusive
- How many nodes can we have? 0 to 10^4 inclusive
- What do we return if we have empty tree? 0
- Is the tree always balanced? No
- Space Constraints? O(1)? O(h)?
- Time Constraints? O(n)?

MATCH:
- Use recursion or iterative approach to keep doing down the BT until we hit None from every node

PLAN:
- Recursive approach:
- if not root: return 0
- So we utilize max function and go down and down for each node's descendants, the max function is going to give us the max depth and all we do is just add one, then the recurisve approach will keep adding one when taking a call off from stack
- return max(self.function(node.left),self.function(node.right)) + 1

EVALUATE:
- Had to use AI to find out that I have to utilize max function
- I would say I got 50% of the question because I feel like max function was kind of like the core of this problem and I wasn't able to figure it out
- Still did question relatively faster to first Tree question, 35 minutes to 22 minutes, good improvement
- Time Complexity: O(n)
- Space Complexity: O(h)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.maxDepth(root.right),self.maxDepth(root.left)) + 1