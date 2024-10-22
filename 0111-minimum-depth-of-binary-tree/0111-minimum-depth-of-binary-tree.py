'''
UNDERSTAND:
- Input: Given root of a BT
- Have to find the minimum depth of the BT
- Min Depth means the closest leaf node from the root node
- Leaf node is a node which doesn't have any descendants going down, no left and no right
- Output: return an integer which is the minimum depth
- BT is a tree in which each node has 0-2 nodes
- How many nodes will the BT have? 0 to 10^5
- Is each node value an int? Yes
- How Big? -1000 to 1000

MATCH:
- Recursion or Iterative
- Can use min function to compare our current depth with the minimum one

PLAN:
- Using Recursion
- Base Case: if not root return 0
- Check if either left or right exists, if so we must follow the path
- Lastly return min if both left and right dont exist

EVALUATE:
- Once again didn't get it
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1