# NOTE: This was easy to solve because I had solved: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        lastNode = len(postorder)-1
        root = TreeNode(postorder[lastNode])
        mid = inorder.index(postorder[lastNode])
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right= self.buildTree(inorder[mid+1:], postorder[mid:lastNode]) # could use postorder[mid:-1] as well

        return root
