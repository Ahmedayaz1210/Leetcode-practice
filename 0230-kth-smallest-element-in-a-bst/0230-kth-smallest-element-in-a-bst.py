'''
UNDERSTAND:
- Input: Given root of a BST
- Have to find the kth smallest value in our tree
- Kth smallest value means if for example k = 1, we have to find first smallest value which is aka smallest or the minimum value or if k = number of nodes then obviously the max value
- Return kth smallest as an integer
- TC?
- SC?
- How many nodes? n
- Node.val: >= 0 and <= 10^4
- how big can k be? 1 <= k <= n <= 10^4
- Can k be bigger than num of nodes? No

MATCH:
- For BF we can use dfs and recursion to do this

PLAN BF:
- BF approach can be to use basic DFS, store node values in a list, at the end sort the list and return k-1, TC: O(n log n), SC:O(n)
- But have to do this in O(n) TC
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.li = []
        print(self.li)
        def dfs(node):
            if not node:
                return

            self.li.append(node.val)
            dfs(node.left)
            dfs(node.right)
            return self.li
        dfs(root)
        self.li.sort()
        
        return self.li[k-1]

PLAN OPTIMAL:
- If you technically look BST is already sorted because left is always smaller and right is always bigger
- We can use In order traversal where we traverse over a tree in left -> root -> right manner since this will give us a sorted order from the start because left most has ot be smallest and right most biggest
- Now also we don't need to store all the nodes in a list, rather we can have a counter of nodes we are looping over, just one integer value
- This works because since we are using in order traversal, obviously we will be looping over in ascending order since the start and when our counter reacher the kth node, we can just return it because it is the kth smallest in our loop
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0
        def dfs(node):
            if not node:
                return 
            left = dfs(node.left)
            if left is not None:
                return left
            self.counter += 1
            if self.counter == k:
                return node.val
            right = dfs(node.right)
            return right
        return dfs(root)
        