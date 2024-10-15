'''
UNDERSTAND:
- Input: Given root nodes ot two binary trees p and q
- Have to see if both of the Binary trees are exactly identical to each other or not
- Identical: has the exact same structure of nodes and those nodes have the exact same value, so it the root node of p has a value of 1, q's root node needs to have a value of 1 as well, so on
- Output: A boolean value, if trees are same: return else if not not at any point return False instantly
- Is this a BT? Yes
- By structure it means that nodes have to be in the same position in both trees? Yes
- Tree is represented by nodes? Yes
- How many nodes can we have? [0,100]
- If we have empty tree, do we return True? Yes
- Each node has an int value? Yes
- How big? -10^4 to 10^4
- A BT can have between 0-2 nodes? Yes

MATCH:
- We can use recursion to loop over the the trees and see if every node matches

PLAN:
- Using recursion
- Base Case: if not root: return True
- Checking for the same value: 
    - if p.val != q.val: return False
- Checking for the same structure:

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: 
            return True
        if not p or not q:
            return False
        
        
        
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left,q.left) and p.val == q.val
        
        