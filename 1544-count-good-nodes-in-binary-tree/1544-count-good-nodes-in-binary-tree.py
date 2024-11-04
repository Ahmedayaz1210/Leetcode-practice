'''
UNDERSTAND:
- Input: Given root of a BT
- Have to find number of good nodes
- A node is considered a good node if from root to that node none of the node's value was greater than the current node X
- Output: Return number of good nodes as an integer number
- TC?
- SC?
- BT can have 0-2 nodes as descendants right
- Nodes can be from 1 - 10^5
- Each node's value can be between [-10^4, 10^4]

MATCH:
- Since we have to go till the depth and look at all the nodes we can use DFS
- Recursion

PLAN:
- Initialize numOfGoodNodes variable to 0
- Use a helper dfs function
- if not node: return : good nodes + 1
- if not.val >= max value in path so far
- max value in path = max(max value in path up till the current node, current node's val)
- left = func(root.left, max so far)
- right = func(root.right, max so far)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.numOfGoodNodes = 0

        def dfs(node, max_so_far):
            if not node:
                return

            if node.val >= max_so_far:
                self.numOfGoodNodes += 1

            max_so_far = max(max_so_far, node.val)

            left = dfs(node.left, max_so_far)
            right = dfs(node.right, max_so_far)

            return self.numOfGoodNodes

        dfs(root, float('-inf'))
        return self.numOfGoodNodes