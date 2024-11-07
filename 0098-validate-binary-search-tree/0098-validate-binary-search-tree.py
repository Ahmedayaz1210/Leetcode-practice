'''
UNDERSTAND:
- Input: Given root of a BST
- Have to validate the BST
    - All nodes on the left have to be smaller than the root
    - All nodes on the right have to be greater than the root
    - Even the subtrees have to be a BST, so rules apply to all
- Output: Boolean value True if valid BST (meets all the requirements) else False (if doesn't)
- TC?
- SC?
- Each node can have 2 descendants
- Num of nodes: 1 to 10^4 so atleast 1 node is there
- Node.val" -2^31 to 2^31
- If we have only one node we return true

MATCH:
- Since we are looking down each path from the root node we can use DFS
- Recursion

PLAN:
- dfs (node, lower_bound, upper_bound):
- if not root: return True
- check_subtree = node.val > lower_bound and node.val < upper_bound
- if  not check_subtree: return false
- return dfs(node.left, lower_bound, node.val) and dfs(node.right, node.val, upper_bound)
- dfs(root, float('-inf'), float('inf'))

EVALUATE:
- Pretty much did the problem myself logic building wise, AI helped with identifying that we need lower and upper bounds as a strategy
- TC: O(n)
- SC:O(h)

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower_bound, upper_bound):
            if not node:
                return True

            check_subtree = node.val > lower_bound and node.val < upper_bound

            if not check_subtree:
                return False

            return dfs(node.left, lower_bound, node.val) and dfs(node.right, node.val, upper_bound)

        return dfs(root, float('-inf'), float('inf'))
        