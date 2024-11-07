'''
UNDERSTAND:
- 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        def bfs(root):
            if not root:
                return
            queue = [root]
            while queue:
                node = queue.pop(0)
                values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        # Collect values using BFS
        bfs(root)
        # Sort values and return kth (1-indexed)
        values.sort()
        return values[k-1]