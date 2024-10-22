'''
UNDERSTAND:
- Input: Given root of a BT
- Have to check if left side of the tree from root node mirrored occurs on right see of tree or not
- Output: Boolean value True if exact mirror else False
- Symmetric means that if a node is on the left side of the left subtree, it has to be on the right side of the right subtree
- Pretty much checking if the left of the tree == right of the tree
- If given empty or one node we return True
- TC?
- SC? 
- Each BT has [1,1000] nodes
- Each Node's value can be <= -100 and >= 100

MATCH: 
- Recursion

PLAN:
- Can use a helper function to check both left and right sides
- It's the same question as same Tree but this time we are checking between left and right sides of a single tree
- Base case: if both don't exist return True meaning they are maintaining same shape
- Base case: if one exists and other doesn't return False
- Check if our current left and right nodes have the same value, put this statement first so if it's false we don't need to go further down rather than going down first
- Then do recursion over left and right of the tree, we use twice because we check lefts all lefts and rights all rights and lefts all rights and rights all lefts

EVALUATE:
- TC: O(n)
- SC: O(n)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right)