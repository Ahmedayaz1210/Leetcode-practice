'''
UNDERSTAND: 
- Input: Given a Binary Tree's root node
- Have to find if the BT is balanced
- Balanced? For every node in the tree, the heigh of it's left subtree and height of its right subtree do not differ by 1
- For ex: In ex 1 we have 9 and 20, 20 has height of 1 and 9 has 0 so 1 - 0 is 1 which is not greater than 1
- Ouput: If difference greater than 1 at any point return False else in the end return True
- A BT can only have between 0-2 descendant nodes right?
- So the tree is only represented by connected nodes?
- Each node has an int value?
- How big?-10^4 to 10^4
- How many nodes?0-5000
- Any space constraints?
- Any Time constraints?

MATCH:
- Pretty much we can use recursion over here to find the height of the binary tree
- So it's either iterative approach or recursive approach, let's go with recursive
- It's pretty much the same question as finding the maximum depth of a BT

PLAN:
- Find height of left of a node and right of a node and if the difference is more than 1 return false, else in the end return true
- Base case: if not root return True
- find height of left 
- find height of right
- check if the difference of heights goes above 1: return False
- return True
- Can create helper function to find the height of the BT
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.right), height(root.left))
        if not root:
            return True
            
        rightHeight = height(root.right)
        leftHeight = height(root.left)

        return (abs(leftHeight - rightHeight) <= 1 and 
        self.isBalanced(root.left) and 
        self.isBalanced(root.right))