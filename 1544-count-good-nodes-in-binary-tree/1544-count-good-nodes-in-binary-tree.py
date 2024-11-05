'''
UNDERSTAND:
- Input: Given root of a BT
- Have to find number of good nodes
- A node is considered a good node if from root to that node none of the previous node's value was greater than the current node X
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
- numOfGoodnodes = 0
- helper function (node, max_val_so_far)
- if not root return
- if node.val > max_val_so_far: numOfGoodnodes += 1
- max_val_so_far = max(node.val, max_val_so_far)
- dfs(node.left)
- dfs(node.right)
- return numOfGoodnodes
- dfs(root)
- return numOfGoodnodes

EVALUATE:
- Didn't get the solution myself even though this was basic DFS ...
- TC: O(n)
- SC: O(h)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.numOfGoodNodes = 0
        def dfs(node, max_so_far):
            if not node:
                return

            if node.val >= max_so_far:
                self.numOfGoodNodes += 1

            max_so_far = max(max_so_far, node.val)
            dfs(node.left, max_so_far)
            dfs(node.right, max_so_far)
            return self.numOfGoodNodes

        dfs(root, float('-inf'))
        return self.numOfGoodNodes