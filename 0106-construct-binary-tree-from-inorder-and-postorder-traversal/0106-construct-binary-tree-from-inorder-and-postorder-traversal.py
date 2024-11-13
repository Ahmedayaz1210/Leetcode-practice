# NOTE: This was easy to solve because I had solved: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.hashmap = {num: i for i,num in enumerate(inorder)}

        self.post_idx = len(postorder) - 1

        def dfs(l,r):
            if l > r:
                return None

            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)
            mid = self.hashmap[root_val]
            root.right = dfs(mid + 1, r)
            root.left = dfs(l, mid - 1)
            return root

        return dfs(0,len(inorder)-1)
