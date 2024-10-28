'''
UNDERSTAND:
- Input: Given root of a BT
- Have to check if the tree is symmetric or not from the root node
- A symmetric tree is a tree in which a node which is on the left side of it's root node in the left side of the tree and the other node would be on the right on the right side of the right tree
- So it is like an opposite for the same Tree problem, kind of
- TC?
- SC?
- How many nodes can we have? [1,1000]
- How big can each Node.val be? -100 to 100
- An empty tree is a symmetric tree
- A single node is a symmetric tree

MATCH:
- Recursion

PLAN:
- if not root: return True
- Can make a helper function to validate the symmetric structure on the left side and right side of the tree
- Base Case: if not left and not right: return True
- Base Case 2: if not left or not right: return False
- Need to check values, if left's value == right's value 
- Need to check same structure, if left structure == right structure
- return helper function with root.left and root.right


EVALUATE:
- Did this question in 15 minutes by myself, tried a tree question after a week because I took a step back to learn some tree question tips and tricks with AI so that defnitely helped
- TC: O(n), n being number of nodes
- SC: O(h), height of the tree
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def dfs(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False

            return left.val == right.val and dfs(left.left,right.right) and dfs(left.right,right.left)

        return dfs(root.left,root.right)