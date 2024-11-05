'''
UNDERSTAND:
- Input: Given root of a BT
- Have to look at the BT as I am looking at it from the right side and only return those nodes
- So seems like returning all of the right most nodes
- Output: return a list of integer node values 
- TC?
- SC?
- How many nodes? [0,100]
- Node.val? -100 to 100 inclusive
- If we have no nodes we return an empty list
- Poor examples: Actually it is not just the right nodes, if we don't have right nodes, we can still see the left ones from the right side
- So now we need to check if right doesn't exist but left does, we append left


MATCH:
- DFS because we are trying to go from top to bottom exploring just the right nodes
- Recursion

PLAN:
- Initialize the result list
- Base case: if not root return []
- Helper DFS function (node):
    - if not node: return
    - result.append(node.val)
    - DFS(node.right)
- DFS(root)
- return result
- Now I need to check if right exists, then append it but if for the same level, right doesn't exist, append the left one
- Examples was bad, I figured we need to use BFS since at each level we are exploring both right and left (if right doesn't exist we would need this)
- USING BFS
- Same template for BFS which I used to Level order traversal 
- Looping by the length of each level
- Since we only want to append the right most node at the level we check if our i == length because that means we have the last node at that level and we want to append that
- Then lastly we append the children of our current nodes

EVALUATE:
- Got 60% of the question, I could've gotten all of this since I knew I had to use BFS and has most of the algorithm done besides the main functionality of appending i == length node which I would say makes 40% of the question
- TC: O(n)
- SC: O(n)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        res = []
        queue.append(root)
        while queue:
            level = len(queue)
            for i in range(level):
                node = queue.popleft()
                if i == level - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res