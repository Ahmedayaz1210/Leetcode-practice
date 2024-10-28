'''
UNDERSTAND:
- Input: Given root of a BT
- Have to return back the root the binary tree in a list of integers by changing the structure of the BT into inorder traversal
- Inorder traversal is: Left node, Root node and Right node
- A BT can have 0-2 descendants for each root node
- Empty Tree: return empty tree
- 1 Node: return that node
- Num of nodes: [0.100]
- Node.val: -100 to 100

MATCH:
- Recursion

PLAN:
- Base case: if not root: return []
- Can utilize a global array to keep track of our traversal
- Because of the global array can create a helper function
- Helper function takes in a root node for parameter
- Base Case: if not root: return (don't have to return an empty list because we are using a global list now)
- helper function (root.left)
- array.append(root.val)
- helper function (root.right)
- return array
- return array
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        def dfs(node):
            
            if not node:
                return

            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
            return result
        
        dfs(root)
        
        return result
        