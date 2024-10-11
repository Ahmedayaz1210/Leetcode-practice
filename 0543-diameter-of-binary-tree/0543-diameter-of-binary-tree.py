# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def dfs(root):
            if not root:
                return 0

            max_left = dfs(root.left)
            max_right = dfs(root.right)

            self.result = max(self.result, max_right+max_left)
            return 1 + max(max_right,max_left)

        dfs(root)
        return self.result
        
        
