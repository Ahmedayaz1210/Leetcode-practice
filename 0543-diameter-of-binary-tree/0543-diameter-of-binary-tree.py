'''
UNDERSTAND: 
- Input: root of a binary tree
- Output: return diameter of the binary tree
- Diameter? length of the longest path between any two nodes in a tree, they can be anywhere in the tree doesn't matter if it's right or left side
- The path may or may not pass through the root node, possibility that might have to go either whole left or right side of the tree
- Length is counted by number of edges between the nodes
- Have to take every node and calculate how far can we go around our tree and find the furthest node by the number of edges
- Tree is represented by nodes? Yes
- Each node has an int value? Yes
- How many nodes? [1,10^4]
- How big can each node value be? -100 to 100 inclusive
- We are returning an int?
- What if empty tree? return 0
- Longest path is always going to be between leaf nodes
- Even if we have one node. we return 0 because there are no edges
- So pretty much counting the edges

MATCH:
- We can use iterative or recursion over here to keep going down and find our longest path
- Longest length tells me that I can use max function to find longest path
- How about finding longest paths from both sides and adding them up?

PLAN:
- Will be using recursion
- Base case: if not root return 0
- Find max on right side
- Find max on left side
- Add them up + 1 (root node)
- return diameter

EVALUATE:
- A bit hard question, I got the logic completely correct, saw a pattern of recursion and knew we had to find max heights (longest path) from both sides and add them up
- Only thing I got confused on was I didn't know how to create a global variable to keep track of max diameter because if I initialized it to 0 it would've became 0 in each recursion so trick was to use a helper method and pretty much compute height in it and max diamater but return max diameter in the original function
- Time Complexity: O(n)
- Space Complexity: O(h)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def dfs(root):
            if not root:
                return 0

            max_left = dfs(root.left)
            max_right = dfs(root.right)

            self.result = max(self.result, max_right+max_left)
            return 1 + max(max_right,max_left)

        dfs(root)
        return self.result
        
        
