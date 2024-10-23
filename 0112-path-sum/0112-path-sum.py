'''
UNDERSTAND:
- Input: Given root of a BT and an integer targetSum
- Have to look for all paths from the root node to leaf nodes and see if any path's node values sum up to our target sum
- Output: Return True if we find a path else if we don't find a path within the whlle tree return False
- TC?, SC?
- How many nodes? 0 to 5000
- How big can each val be? -1000 to 1000
- How big can target sum be? -1000 to 1000
- Remember it has to be root to leaf, can't finish before

MATCH:
- Recursion

PLAN: 
- 1. Identify our root to leaf paths
- 2. Do summation of all the nodes in the path
- 3. If it equals target sum instantly return True
- 4. Else in the end if no such path found retunr False

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currSum):
            if not node:
                return False

            currSum += node.val
            if not node.left and not node.right:
                return currSum == targetSum

            return (dfs(node.left, currSum) or dfs(node.right, currSum))

        return dfs(root,0)
        
