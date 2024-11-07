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
- how big can k be? 1 <= k <= n <= 104
- Can it be bigger than num of nodes? No

MATCH:
- We can use BFS to store nodes at each level
- DFS can be used to
- Queue for BFS

PLAN:
- BF approach can be to store the nodes in a list, then sort them and return k-1 position element. TC: O(n log n), SC: O(n)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
            

