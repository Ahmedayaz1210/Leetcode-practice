'''
UNDERSTAND:
- Input; Given root of a BT
- BT has between 0-2 nodes
- The given BT is in a form of root, left, right
- Have to find inorder traversal
- Inorder Traversal is return the BT in a form left, root, right so left node comes first then root and then right
- We have to go to depth of the tree for each node such as in example 2 left most node is 4
- Output: return the tree's root node but this time tree is arranged in inorder traversal, returning nodes.val in a list
- Empty Tree: return empty tree
- Tree has only one node: return just that
- TC?
- SC?
- How many nodes can we have in total? 0 to 100
- How big is the value of each node? -100 to 100

MATCH:
- Since we are finding nodes from the root's depth we can use recursion or iteration
- I will go with recursion

PLAN:
- create global list function
- create a helper function to go in depths
- base case: if no root then just simple return because we are not appending null values
- call this on left
- append the root val 
- call on right
- return list

EVALUATE:
- I was trying to append left and right both into list but we only need to append root because when the base case hits both left and right will be none so in that case we jus return root.val and then form there it builds up
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li = []
        def dfs(root):
            if not root:
                return

            dfs(root.left)
            li.append(root.val)
            dfs(root.right)
        dfs(root)
        return li