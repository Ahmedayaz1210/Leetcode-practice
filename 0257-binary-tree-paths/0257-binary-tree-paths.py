# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self.dfs(root, "", res)
        return res
        

    def dfs(self, root, s, res):
        
    
        if s != "":
            s += "->"
        s += str(root.val)
        print(s)

        if not root.left and not root.right:
            res.append(s)

        if root.left:
            self.dfs(root.left, s, res)
        if root.right:
            self.dfs(root.right,s,res)

        
        