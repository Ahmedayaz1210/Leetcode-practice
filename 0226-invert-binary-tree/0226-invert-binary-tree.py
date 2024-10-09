'''
UNDERSTAND:
- Input: Given root node of a binary tree
- Binary Tree is a tree where each node can have at most two descendant nodes
- Have to invert the binary tree
- Invert? Flip on y axis or mirror the tree out
- Nodes on the right go to the left side and vice versa
- Have to return back the root of the tree
- Tree is represented by nodes
- Tree can have 0 - 100 nodes inclusive
- How big can each node.val be? -100 to 100
- Given emoty BT? Return None
- Is the tree always going to be balanced? meaning equal nodes on both of the sides
- Nodes can have null children? Yes
- Moving around the nodes themselves and not the values?
- Each node has value, left and right parameters

MATCH:
- Can use recursion or iterative approach
- I will use recursion

PLAN:
- Base case: If empty tree: return None
- We do recursion over the tree
- Place left in temp variable before cutting off conection
- left = right
- right = temp
- send both pointers to recursion
- return root

EVALUATE:
- First Tree question so took me 33 minutes but it was simple
- Time complexity: O(n) since visiting each node
- Space Complexity: O(h), h is height because could be O(log n) if balanced and if skewed to one side O(n)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)    

        return root    