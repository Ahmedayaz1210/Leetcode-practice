'''
UNDERSTAND: 
- Input: Given a Binary Tree's root node
- Have to find if the BT is balanced
- Balanced? For every node in the tree, the heigh of it's left subtree and height of its right subtree do not differ by 1
- For ex: In ex 1 we have 9 and 20, 20 has height of 1 and 9 has 0 so 1 - 0 is 1 which is not greater than 1
- Ouput: If difference greater than 1 at any point return False else in the end return True
- A BT can only have between 0-2 descendant nodes right?
- So the tree is only represented by connected nodes?
- Each node has an int value?
- How big?-10^4 to 10^4
- How many nodes?0-5000
- Any space constraints?
- Any Time constraints?

MATCH:
- Pretty much we can use recursion over here to find the height of the binary tree
- So it's either iterative approach or recursive approach, let's go with recursive
- It's pretty much the same question as finding the maximum depth of a BT

PLAN:
- Find height of left of a node and right of a node and if the difference is more than 1 return false, else in the end return true
- Base case: if not root return True
- find height of left 
- find height of right
- check if the difference of heights goes above 1: return False
- Also check if both left and right subtrees are balanced for all of the nodes using recursion
- Can create helper function to find the height of the BT
- O(n^2) solution:
def height(root):
            if not root:
                return 0
            return 1 + max(height(root.right), height(root.left))
if not root:
    return True
    
rightHeight = height(root.right)
leftHeight = height(root.left)

return (abs(leftHeight - rightHeight) <= 1 and 
self.isBalanced(root.left) and 
self.isBalanced(root.right))

EVALUATE:
- Time Complexity: O(n^2), we're calculating the height of its left and right subtrees, for skewed can be O(n^2) in worse scenario
- Space Complexity: O(h)
- I didn't get the question, it was fairly tricky but calculating the height part wasn't 
- I got confused on why we had to check isBalanced for both right and left in the return statement but that's because we need to check for all of the nodes if they are balanced not just the difference. 
- Why we need self.isBalanced(root.left) and self.isBalanced(root.right):

Purpose: These checks ensure that every subtree in our binary tree is balanced, not just the current node.
Simple analogy:
Imagine you're checking if a family tree is "balanced" (everyone has 0-2 children). You can't just check the first person; you need to check everyone in the tree.
Example:
Let's look at this tree:
    1
   / \
  2   3
 /     \
4       5
         \
          6

At node 1: The height difference is 1 (left subtree height 2, right subtree height 3). This seems balanced.
But the right subtree (3-5-6) is not balanced!


What happens without these checks:

We'd only check the height difference at each node.
We'd miss the imbalance in the subtree (3-5-6).


What these checks do:

self.isBalanced(root.left): Checks if the entire left subtree is balanced.
self.isBalanced(root.right): Checks if the entire right subtree is balanced.


Simple explanation:

It's like saying: "This node is balanced AND all its children are balanced too."
If any part of the tree is unbalanced, the whole tree is considered unbalanced.

Neetcode's O(n) SC solution: see code

Key differences in O(n^2) and O(n) approach:

Redundant Calculations:

O(n²): The height function is called separately for each node, potentially recalculating heights for the same subtrees multiple times.
O(n): Height and balance are calculated in a single pass, avoiding recalculations.


Information Propagation:

O(n²): Only balance information is propagated up the tree. Height is recalculated for each node.
O(n): Both height and balance information are propagated up the tree simultaneously.


Early Termination:

O(n²): Continues checking even if an imbalance is found deep in the tree.
O(n): Can terminate early if an imbalance is found, as the balanced flag is passed up.


Number of Traversals:

O(n²): In the worst case (a balanced tree), it traverses the tree multiple times - once for each node's balance check.
O(n): Always traverses the tree exactly once, regardless of its structure.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = (abs(left[1] - right[1]) <= 1 and left[0] and right[0])
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
