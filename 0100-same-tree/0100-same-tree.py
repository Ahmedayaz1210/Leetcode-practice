'''
UNDERSTAND:
- Input: Given root nodes ot two binary trees p and q
- Have to see if both of the Binary trees are exactly identical to each other or not
- Identical: has the exact same structure of nodes and those nodes have the exact same value, so it the root node of p has a value of 1, q's root node needs to have a value of 1 as well, so on
- Output: A boolean value, if trees are same: return else if not not at any point return False instantly
- Is this a BT? Yes
- By structure it means that nodes have to be in the same position in both trees? Yes
- Tree is represented by nodes? Yes
- How many nodes can we have? [0,100]
- If we have empty tree, do we return True? Yes
- Each node has an int value? Yes
- How big? -10^4 to 10^4
- A BT can have between 0-2 nodes? Yes

MATCH:
- We can use recursion to loop over the the trees and see if every node matches

PLAN:
- Using recursion
- Base Case: if not root: return True
- Checking for the same value: 
    - if p.val != q.val: return False
- Checking for the same structure: 
    - send both left and right of each back to function

EVALUATE: 
- Let's say - n: num of nodes in p, m: num of nodes in q
- TC: O(p+q)
- SC: O(p+q)
- I got 75% of the question I would say
- MISTAKE: I made the mistake of not including the second if statement
    - So the first statement checks if they both have reached the leaf nodes and returns True
    - But this statement doesn't check if one is bigger than the other and keeps on returning True for it as well, If the function tries to access p.val when p is None, it would raise an error (like AttributeError in Python). If the function is written to handle this case without raising an error, it might continue recursing, potentially returning True incorrectly if the rest of the subtree in q matches the structure it's expecting.
    - Second one checks if one is bigger than the other, for example if they are the exact same trees but one has an extra node down there that other doesn't in that case we need to return False and first statement doesn't check it
   1                1
  / \              / \
 2   3            2   3
      \
       4               

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: 
            return True
        if not p or not q:
            return False
        
        
        
        return  p.val == q.val and self.isSameTree(p.right, q.right) and self.isSameTree(p.left,q.left)
        
        