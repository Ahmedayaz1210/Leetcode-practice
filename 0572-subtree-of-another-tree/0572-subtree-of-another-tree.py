'''
UNDERSTAND:
- Input: Given root nodes of 2 BTs "root" and "subroot"
- Have to check if all of the subroot tree exists somewhere in root tree with 2 conditions
    - Same node values
    - Same structure
- Same question as "same tree"
- Output: if subroot exists return True else False
- The root tree can be a subtree of itself
- BT consists of nodes linked together 
- A BT can have between 0-2 descendants
- Each node has an integer value
- How big is the root? [1,2000]
- How big is subroot? [1,1000]
- How big can value be in root? -10^4 to 10^4
- How big can value be in subroot? same thing ^

MATCH:
- Can use recursion
- Applying the same knowledge as same tree question

PLAN:
- Might need a helper function 
- If not root and not subroot: return True
- If not root or not subroot: return False
- If root.val != subroot.val: return False
- Check if they are the same structure

EVALUATE:
- TC: O(len(root)*len(subRoot)) because for each node of root we might need to check all of subroot
- SC: O(len(root)) because in the worst case we might store the calls for height of root
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        
        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False

        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right) and root.val == subRoot.val