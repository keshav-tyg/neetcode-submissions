# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #dont need value of tree
        #max depth of both sides and add them
        max_diameter = 0
        def height(node):
            nonlocal max_diameter
            if node == None: return 0

            left_try = height(node.left)
            right_try = height(node.right)
            max_diameter = max(max_diameter, left_try + right_try)
            return 1 + max(left_try, right_try)
        height(root)
        return max_diameter

