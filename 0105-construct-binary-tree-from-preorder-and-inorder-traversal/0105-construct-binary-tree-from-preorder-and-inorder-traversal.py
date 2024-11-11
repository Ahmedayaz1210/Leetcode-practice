'''
UNDERSTAND:
- Input: Given two integer lists of our BT traversal, one is preorder and other is inorder
- Preorder is root -> left -> right sequence
- Inorder is left -> root -> right sequence
- Have to use these two sequences and do reverse engineering and construct our original BT from which these two were made
- Output: Return head of our original BT
- TC?
- SC?
- Number of nodes? >= 1 and <= 3000
- Node.val? [-3000, 3000] Inclusive
- Pre order and In order are going to be the same length? Which means same length BT? yes
- Both orders will have same node values right? Just different order? Yes same values and no value will repeat.
- Both definitely exist in our original BT
- Do we append null values in our BT?

MATCH:
- Use Recursion to create our BT by looping over our arrays on Inorder and Preorder traversal

PLAN:
- Base case: if not preorder or not inorder: return None (we know we looped over them, just check either of these because they will be the same length)
- Our root node will always be the sliced preorder's 0th index because that's how it starts from the very first loop as the sequence is root, left, right
- Get our root's index in inorder, so we know everything to it's left is our left tree and everything to it's right is our right tree
- Now send back left and right into our function for recursion
    - For left the preoder will be 1 to mid + 1 because everything inorder is left, root, right. The inorder will be 0th to mid but not including mid because that's our node
    - For right it will be the opposite, for preorder it's mid+1 till the end because everything to mid's right is our right tree and for inorder it's the same.

EVALUATE:
- Couldn't solve this question, it was tricky and hard, had to observe preorder and inorder closely to find the pattern
- TC: O(n^2) because for each preorder root we have to find it in inorder. Better explanation if confused: https://claude.ai/chat/bc64ebc3-556b-4c0d-852b-eb7816a9c3ff
- SC: O(n^2) because O(n) for recursion stack and O(n) in worst case for storing our sublists like a skewed right tree where each sublist is just in right call. For better understanding check: https://chatgpt.com/g/g-cKXjWStaE-python/c/67323a90-c404-8003-9710-24f1a0e26dfd
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
