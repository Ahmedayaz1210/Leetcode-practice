'''
UNDERSTAND:
- Input: Given root of a BST and two other nodes p and q
- Have to find the Lowest Common Ancestor for the nodes p and q
- LCA: From all the root nodes of p and q, LCA node would be the one which is their first parent
- A BST is a tree where all the left values are smaller than the root node and all the right values are bigger than the root node
- Output: return the LCA node so returning a node
- TC?
- SC?
- Node.val: -10^9 to 10^9
- All node values are distinct? Yes
- How many nodes? [2,10^5]
- Can p and q be the same node? No
- What happens if no node is there? p and q have to exist
- What if we only have two nodes? Then current node is our LCA so in example 2 it is like 2, 2 is LCA
                                                                                         /
                                                                                        1

MATCH:
- Recursion

PLAN:
- So in a BST we know left values are going to be smaller than root which is going to be smaller than right values
- Since we have both p and q guaranteed we don't need a base case
- if p.val and q.val < root.val:
    return LCA(root.left,p,q)
- else if p.val and q.val > root.val:
    return LCA(root.right,p,q)
- else (one is smaller and one is bigger means root is our LCA): return root

EVALUATION
- Wasn't a very hard question
- Took 25 minutes to solve it
- First question on BST rather than only BT so had to use AI to understand the difference between the two and in a BST left node.val is always < root node.val is always < right node.val
- This way AI kind of gave me a hint of the conditional statements so I would say I did 70% of the problem myself
- TC: O(n) x it's actually O(h) because since it is BST we only go down one path (left or right) so in the worse it could go to all nodes when it's skewed but it is still O(h), in normal BT it would be O(n) because we don't know when value is smaller or bigger so we end up recursion all nodes in worst case
- SC: O(h)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)

        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)

        return root